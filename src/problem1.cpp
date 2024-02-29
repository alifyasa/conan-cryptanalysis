// Asumption: input string only contains capital letter
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll arr[26];
void solve(){
    freopen("../test/input/problem1.txt", "r", stdin);
    freopen("../test/output/problem1.txt", "w", stdout);
    string s; cin >> s;
    ll szS = s.length();
    // Do frequency count first for each character on string
    for(ll i = 0; i < szS; i++){
        arr[s[i] - 64]++;
    }
    // We can show the frequency count of each character
    for(ll i = 1; i <= 26; i++){
        cout << (char)(i + 64) << " " << arr[i] << "\n";
    }
    // We can rank the frequency from the highest to the lowest with bigram and trigram list
    

}
 
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
 
    solve();
 
    return 0;
}