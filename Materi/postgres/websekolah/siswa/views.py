
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.utils.html import escape

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    """Mengubah satu hasil query menjadi dictionary."""
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return dict(zip(columns, row))


def siswa_list(request):

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tgl_lahir, status_hadir, nilai_akhir
            FROM siswa
            ORDER BY id DESC
        """)
        data_siswa = dictfetchall(cursor)

    # return HttpResponse(html)
    return render(request, 'list.html', {'keyword': 'ini siswa nya pak!', 'data': data_siswa})

def siswa_detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tgl_lahir, status_hadir, nilai_akhir
            FROM siswa
            WHERE id = %s
        """, [id])
        siswa = dictfetchone(cursor)
    return render(request, 'detail.html', {'siswa': siswa})



def siswa_create(request):
    # cek request yg masuk, klo dia POST (submit)
    if request.method == 'POST':    
        #debug mode
        print("debug POST request:", request.POST.dict())    
        # kumpulkan data dari request post
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()
        tgl_lahir = request.POST.get('tgl_lahir', '').strip()
        status_hadir = request.POST.get('status_hadir', '').strip()
        nilai_akhir = request.POST.get('nilai_akhir', '').strip()

        # eksekusi query insert ke tabel siswa
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO siswa (nama, umur, tgl_lahir, status_hadir, nilai_akhir)
                VALUES (%s, %s, %s, %s, %s)
                """,
                [nama, umur, tgl_lahir, status_hadir, nilai_akhir]
            )

        # klo berhasil maka redirect ke siswa list
        return redirect('siswa_list')

    # klo gk submit (GET)
    return render(request, 'form.html')



def siswa_update(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tgl_lahir, status_hadir, nilai_akhir
            FROM siswa
            WHERE id = %s
        """, [id])
        siswa = dictfetchone(cursor)

    if siswa and siswa['tgl_lahir']:
        siswa['tgl_lahir'] = siswa['tgl_lahir'].strftime('%Y-%m-%d')

    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip() or siswa['nama']
        umur = request.POST.get('umur', '').strip() or siswa['umur']
        tgl_lahir = request.POST.get('tgl_lahir', '').strip() or siswa['tgl_lahir']
        status_hadir = request.POST.get('status_hadir', '').strip() or siswa['status_hadir']
        nilai_akhir = request.POST.get('nilai_akhir', '').strip() or siswa['nilai_akhir']

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE siswa
                SET nama = %s, umur = %s, tgl_lahir = %s, status_hadir = %s, nilai_akhir = %s
                WHERE id = %s
            """, [nama, umur, tgl_lahir, status_hadir, nilai_akhir, id])

        return redirect('siswa_list')

    return render(request, 'edit.html', {'siswa': siswa})


def siswa_delete(request, id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tgl_lahir, status_hadir, nilai_akhir
            FROM siswa
            WHERE id = %s
        """, [id])
        siswa = dictfetchone(cursor)

    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM siswa WHERE id = %s", [id])
        return redirect('siswa_list')

    return render(request, 'delete.html', {'siswa': siswa})