    GAME TURN BASE PYTHON BERBASIS TERMINAL
----------------------------------------------
## Deskripsi
Game yang meminta pemain membuat karakter dan memasukkan keputusan,
dibangun dengan Python dan dijalankan di Terminal

## Tujuan Game
Membuat keputusan yang benar dan mennghabiskan seluruh Health Point musuh untuk mendapatkan kemenangan

## Mekanisme Player
-------------------
# Membuat Karakter
Pemain diminta untuk memasukkan nama karakternya atau menggunakan nama defaultnya (Kevin)

# Menampilkan Health Point
Papan game akan secara realtime terus memperbarui status Health Point karakter maupun musuh secara berkala begitu selesai membuat keputusan

# Membuat Keputusan
Player akan selalu diminta membuat keputusan saat melanjutkan game, memilih untuk menyerang mengakibatkan damage bagi musuh atau memilih bertahan untuk memulihkan Health Point

## Menyerang
-------------
Jika player memilih menyerang maka akan mengakibatkan damage acak yang akan mengurangi Health Point musuh

## Bertahan
-----------
Jika player memilih untuk bertahan maka akan memulihkan secara acak Health Pointnya sendiri

## Health Point 
---------------
Health Point adalah nyawa yang dimiliki baik player maupun musuh, Health Point harus dijaga oleh player untuk memenangkan pertandingan, selalu memperhatikan kondisi Health Point akan membantu membuat keputusan yang tepat

## Serangan Musuh
------------------
Musuh akan selalu menyerang memberikan damage acak ke Health Point player selama satu putaran

## Satu Putaran
----------------
Setiap satu putaran, player akan ditampilkan jumlah Health Pointnya dan musuhnya, lalu diminta membuat satu keputusan untuk menyerang atau bertahan, disisi lain musuh akan selalu menyerang player, akan selalu berulang hingga Health Point salah satu player atau musuh habis

## Game Selesai
---------------
# Menang 
Jika Health Point player masih ada dan Health Point musuh habis, maka game dinyatakan menang bagi player

# Kalah
Jika Health Point player habis sedangkan Health Point musuh masih tersisa, maka game dinyatakan kalah bagi player

## Detail Teknis
----------------

