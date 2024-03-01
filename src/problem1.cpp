// Asumption: input string only contains capital letter
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct gramItem {
    string gram;
    int count;
};

struct trigramPost{
    int first;
    int second;
    int third;
};

struct bigramPost{
    int first;
    int second;
};

ll arrUnigram[36], arrBigram[36][36], arrTrigram[36][36][36];
ll countValueUnigram[36], countValueBigram[36*36], countValueTrigram[36*36*36];
char firstChar,secondChar;
int convertHashFromChar(char c){
    int temp = (int)c;
    if(temp >= 65) return temp-65;
    else return temp-22;
}
char convertHashFromInt(int n){
    if(n < 26) return (char)(n+65);
    else return (char)(n+22);
}
void solve(){
    freopen("../test/input/problem1.txt", "r", stdin);
    freopen("../test/output/problem1.txt", "w", stdout);
    string temp;
    string tempLast2 = "XX";
    int lengthPlainText = 0;
    // Keep reading lines until an empty line is encountered
    int countDebug=0;
    while(getline(cin, temp)&&!temp.empty()) {
        countDebug++;
        ll tempLengthTemp = temp.length();
        for(int i = 0; i < tempLengthTemp; i++){
            arrUnigram[convertHashFromChar(temp[i])]++;
            if(lengthPlainText%2==1){
                firstChar = tempLast2[1];
                if(i>0) firstChar = temp[i-1];
                arrBigram[convertHashFromChar(firstChar)][convertHashFromChar(temp[i])]++;
            }
            if(lengthPlainText%3==2){
                firstChar = tempLast2[0];
                secondChar = tempLast2[1];
                if(i>1) firstChar = temp[i-2];
                if(i>0) secondChar = temp[i-1];
                arrTrigram[convertHashFromChar(firstChar)][convertHashFromChar(secondChar)][convertHashFromChar(temp[i])]++;
            }
            lengthPlainText++;
        }
        tempLast2 = "";
        tempLast2 += temp[tempLengthTemp-2];
        tempLast2 += temp[tempLengthTemp-1];
    }

    // Using counting sort to sorting the frequency of unigram, bigram, and trigram
    ll countValueUnigram[lengthPlainText+1];
    ll countValueBigram[lengthPlainText];
    ll countValueTrigram[lengthPlainText-1];
    for(int i = 0; i<=lengthPlainText; i++) countValueUnigram[i] = 0;
    for(int i = 0; i<lengthPlainText; i++) countValueBigram[i] = 0;
    for(int i = 0; i<lengthPlainText-1; i++) countValueTrigram[i] = 0;
    // Count each value of unigram, bigram, and trigram
    for(int i=0; i<36; i++) if(arrUnigram[i]!=0)countValueUnigram[arrUnigram[i]]++;
    for(int i=0; i<36; i++) for(int j=0; j<36; j++) if(arrBigram[i][j]!=0) countValueBigram[arrBigram[i][j]]++;
    for(int i=0; i<36; i++) for(int j=0; j<36; j++) for(int k=0; k<36; k++) if(arrTrigram[i][j][k]!=0) countValueTrigram[arrTrigram[i][j][k]]++;
    // Count cumulative value of unigram, bigram, and trigram using dynamic programming
    for(int i=0; i<36; i++) countValueUnigram[arrUnigram[i]] += countValueUnigram[arrUnigram[i]-1];
    for(int i=0; i<36; i++) for(int j=0; j<36; j++)countValueBigram[arrBigram[i][j]] += countValueBigram[arrBigram[i][j]-1];
    for(int i=0; i<36; i++) for(int j=0; j<36; j++) for(int k=0; k<36; k++) countValueTrigram[arrTrigram[i][j][k]] += countValueTrigram[arrTrigram[i][j][k]-1];

    // Bigram Analysis

    // Trigram Analysis

    // We can rank the frequency from the highest to the lowest with bigram and trigram list


}
 
int main() {
 
    solve();
 
    return 0;
}