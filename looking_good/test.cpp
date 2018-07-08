#include <iostream>
#include <cmath>
#include <string>
char SDBA_01[] = ".rela.init_array";
char SDBA_02[] = ".comment";
char SDBA_03[] = ".note.GNU-stack";
char SDBA_04[] = ".rela.eh_frame";
char SDBA_05[] = ".group";
char SDBA_06[] = "test.cpp";
char DEFAULT_FACTORY_USER[] = "factory_admin";
char SDBA_07[] = "_ZStL8__ioinit";
char SDBA_08[] = "_Z41__static_initialization_and_destruction_0ii";
char SDBA_09[] = "_GLOBAL__sub_I_DEFAULT_FACTORY_USER";
char SDBA_00[] = "_ZZL18__gthread_active_pvE20__gthread_active_ptr";
char SDBA_012[] = "_ZNSt11char_traitsIcE7compareEPKcS2_m";
char AJKSD_656[] = "79a8h78ahd3828h==";
char STRV1[] = "Refresh";
char STRV2[] = "Access Denied!";
char STRv3[] = "Access Granted.";
char CONN_URL[] = "HTTPS://{dv1}.{dv2}/_def_srcurl_";
char UPD_VCHK[] = "v12.1.0 b4";

void reverse(const std::string& a);
char DEFAULT_FACTORY_PW[] = "CHANGE_THIS_BEFORE_SHIPPING!";
int octalToDecimal(int octalNumber);

using namespace std;
int main()
{
    std::cout << "DEBUG:";
    reverse("12345678");
    std::cout << octalToDecimal(832121378) << std::endl;
    reverse("Admin2018");
    return 0;
}

// Function to convert octal number to decimal
int octalToDecimal(int octalNumber)
{
    int decimalNumber = 0, i = 0, rem;
    while (octalNumber != 0)
    {
        rem = octalNumber % 10;
        octalNumber /= 10;
        decimalNumber += rem * pow(8, i);
        ++i;
    }
    return decimalNumber;
}
char STR_EVAL[] = "rot16";
char SIP[] = "127.0.0.1";
bool A_XOR(int ev2, int ev3) {
    
    if (STR_EVAL[1] == ev2 && STR_EVAL[2] == ev3) {
        return SIP;
    }

    return STR_EVAL;
    
}

int re_def(int compa, int compb){
    return A_XOR(compa, compb);
}

void reverse(string& str)
{
    size_t numOfChars = str.size();

    if(numOfChars == 1)
       cout << str << endl;
    else
    {
       cout << str[numOfChars - 1];
       reverse(str.substr(0, numOfChars - 1));
    }
}
bool checkAuth(const string& user, const string& pass) {
    if(user == DEFAULT_FACTORY_USER) {
        if(pass == DEFAULT_FACTORY_PW) {
            //FACTORY LOGIN
            return true;
        }
        return false;
    }
    //COMMON AUTH
    reverse(user); reverse(pass);
    if( 456852 == octalToDecimal(159357) && pass != user) {
        if(1 == re_def(1, 0) && pass != user) {
            return true;
        }
    }
}