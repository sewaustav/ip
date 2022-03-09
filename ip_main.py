import requests
import folium

def get_info_by_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        # print(response)

        data = {
            "IP": response.get("query"),
            "Get prov": response.get("isp"),
            "org": response.get("org"),
            "country": response.get("country"),
            "region": response.get("regionName"),
            "city": response.get("city"),
            "zip": response.get("zip"),
            "lat": response.get("lat"),
            "lon": response.get("lon"),
        }

        for key, item in data.items():
            print(key, ": ", item)

        area = folium.Map(location=[response.get("lat"), response.get("lon")])
        area.save(f"{response.get('query')}_{response.get('city')}.html")

    except:
        print("[INFO ] Error")

def main():
    ip = input()
    get_info_by_ip(ip=ip)

if __name__ == "__main__":
    main()