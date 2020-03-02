// NSE-API.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include  <string>
#include  <fstream>
#include<conio.h>
#include <stdio.h>
#include <algorithm> 
#include<iomanip>
#include "nlohmann/json.hpp"

using namespace std;
using json = nlohmann::json;

FILE* fp1;
json j;

void json_process();
void nse_api();

int main()
{

	nse_api();
	json_process();
	_getch();
}
	
void json_process()
{
	std::ifstream i("sardard.json");
	
	i >> j;

	
	std::ofstream o("formatted_sardard.json");
	o << std::setw(4) << j << std::endl;
	cout <<"[priceInfo][lastProce]=" << j["priceInfo"]["lastPrice"]<<endl;
	cout << "[priceInfo][previousClose]=" << j["priceInfo"]["previousClose"] << endl;
}

void nse_api()
{
	const char* nse_api = "curl -k \"https://www.nseindia.com/api/quote-equity?symbol=EIHOTEL\" -H \"authority: beta.nseindia.com\" -H \"cache-control: max-age=0\" -H \"dnt: 1\" -H \"upgrade-insecure-requests: 1\" -H \"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36\" -H \"sec-fetch-user: ?1\" -H \"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\" -H \"sec-fetch-site: none\" -H \"sec-fetch-mode: navigate\" -H \"accept-encoding: gzip, deflate, br\" -H \"accept-language: en-US,en;q=0.9,hi;q=0.8\" --compressed  -o sardard.json";
	system(nse_api);
}