// Asumption: input string only contains capital letter
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll arr[36];
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
    int count = 0;
    string s; s = "";
    string temp;
    // Keep reading lines until an empty line is encountered
    while (getline(cin, temp)&&!temp.empty()) {
        s += temp;
    }
    ll szS = s.length();

    // Do frequency count first for each character on string
    for(ll i = 0; i < szS; i++){
        arr[convertHashFromChar(s[i])]++;
    }
    cout << s << "\n";

    // We can rank the frequency from the highest to the lowest with bigram and trigram list


}
 
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
 
    solve();
 
    return 0;
}