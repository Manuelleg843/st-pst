# filename = 'bps.csv'
# search_keyword = 'Badan Pusat Statistik until:2023-10-01 since:2023-01-01'
# limit = 5000

# os.environ['MY_API_TOKEN'] ='0d94f81cb49e38b4692746400a9013d835e56613'

# # !npx --yes tweet-harvest@latest -o "{filename}" -s "{search_keyword}" -l {limit} --token "$MY_API_TOKEN"
# # Bentuk perintah shell sebagai string
# command = f'npx --yes tweet-harvest@latest -o "{filename}" -s "{search_keyword}" -l {limit} --token "$MY_API_TOKEN"'

# # Jalankan perintah shell menggunakan subprocess
# try:
#     result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     print("Keluaran (stdout):")
#     print(result.stdout)
    
#     if result.stderr:
#         print("Error (stderr):")
#         print(result.stderr)
#     else:
#         print("Perintah telah berhasil dijalankan tanpa error.")
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")


#MENGUNDUH GAMBAR
    # Widget untuk mengunggah gambar
    uploaded_image = st.file_uploader("Unggah gambar", type=["jpg", "png", "jpeg"])

    # Menampilkan gambar yang diunggah (jika ada)
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Gambar yang diunggah", use_column_width=True)

    # Tombol untuk mengunduh gambar
    if st.button("Unduh Gambar"):
        if uploaded_image is not None:
            # Mengunduh gambar dengan nama yang sama
            with open("downloaded_image.jpg", "wb") as f:
                f.write(uploaded_image.read())
            st.success("Gambar berhasil diunduh dengan nama 'downloaded_image.jpg'")
        else:
            st.warning("Tidak ada gambar yang diunggah untuk diunduh.")



# os.environ['MY_API_TOKEN'] ='0d94f81cb49e38b4692746400a9013d835e56613'
# # !npx --yes tweet-harvest@latest -o "{filename}" -s "{search_keyword}" -l {limit} --token "$MY_API_TOKEN"
# command = f'npx --yes tweet-harvest@latest -o "{filename}" -s "{search_keyword}" -l {limit} --token "$MY_API_TOKEN"'
