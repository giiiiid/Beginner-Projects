import speedtest

def check_speed():
    st = speedtest.Speedtest()
    download = st.download() / 10**6
    upload = st.upload() / 10**6
    print(f'Download speed: {download} MB')
    print(f'Upload speed: {upload} MB')
print(check_speed())
