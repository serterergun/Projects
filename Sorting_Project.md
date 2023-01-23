# Proje 1
[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

Big-O gösterimini yazınız.

Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer?

Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.

[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

# Cevap

**1.Adım**
[22,27,16,2,18,6]

**2.Adım**
[22,27,16,2,18,6]

**3.Adım**
[16,22,27,2,18,6]

**4.Adım**
[2,16,22,27,18,6]

**5.Adım**
[2,16,18,22,27,6]

**6.Adım**
[2,6,16,18,22,27]

# Big-O Notation

İlk adımda n sayıda işlem olduğu için ve takip eden adımlarda n-1 sayıda işlem olduğu için:

n+(n-1)+(n-2)+(n-3)..... = [n(n-1)]/2 = [n^2-n]/2

Domine eden fonksiyon n^2 olduğu için:

Big-O Notation: O(n^2)

18 sayısı dizinin ortasında olduğu için Time Complexity **average case** olur.

[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

**1.Adım**
[2,3,5,8,7,9,4,15,6]

**2.Adım**
[2,3,4,8,7,9,5,15,6]

**3.Adım**
[2,3,4,5,7,9,8,15,6]

**4.Adım**
[2,3,4,5,6,9,8,15,7]




