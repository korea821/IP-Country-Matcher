import requests

# IP 목록 파일 경로
input_file = "bad_ip.txt"
output_file = "bad_ip_with_country.txt"

# IP 조회 API URL
api_url = "https://ipinfo.io/{ip}/json"

# 결과를 저장할 리스트
results = []

# 파일에서 IP 읽기
with open(input_file, "r") as file:
    ip_addresses = file.readlines()

# IP 주소의 국가 정보 가져오기
for ip in ip_addresses:
    ip = ip.strip()  # 공백 제거
    if ip:
        try:
            response = requests.get(api_url.format(ip=ip))
            if response.status_code == 200:
                data = response.json()
                country = data.get("country", "Unknown")
                results.append(f"{ip} - {country}")
            else:
                results.append(f"{ip} - Error: {response.status_code}")
        except Exception as e:
            results.append(f"{ip} - Error: {str(e)}")

# 결과를 파일에 저장
with open(output_file, "w") as file:
    file.write("\n".join(results))

print(f"IP와 국가 매칭 결과가 {output_file}에 저장되었습니다.")
