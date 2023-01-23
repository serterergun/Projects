# Proje 3

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

# Cevap
Dizinin ilk elemanı 7'yi root olarak belirliyoruz. Daha sonra sırasıyla sayıları incelemeye başlıyoruz. 

**1.Adım** 
Dizinin ikinci elemanı 5; root'dan küçük olduğu için root'un soluna yazılır.

            7
           / 
          5   

**2.Adım**
Dizinin üçüncü elemanı 1; 7'den ve 5'den küçük olduğu için 5'in soluna yazılır.

            7
           /
          5  
         / 
        1

**3.Adım**
Dizinin dördüncü elemanı 8, 7'den büyük olduğu için 7'nin sağına yazılır.

            7
           / \
          5   8
         /
        1

**4.Adım**
Dizinin beşinci elemanı 3, 7'den ve 5'den küçük, 1'den büyük olduğu için 1'in sağına yazılır.

            7
           / \
          5   8
         /
        1    
         \
          3

**5.Adım**
Dizinin altıncı elemanı 6, 7'den küçük ve 5'den büyük olduğu için 5'in sağına yazılır.

            7
           / \
          5   8
         / \   
        1   6   
         \
          3

**6.Adım**
Dizinin yedinci elemanı 0; 7'den, 5'den 1'den küçük olduğu için 1'in soluna yazılır.

            7
           / \
          5   8
         / \   
        1   6   
       / \
      0   3

**7.Adım**
Dizinin sekizinci elemanı 9; 7'den ve 8'den büyük olduğu için 8'in sağına yazılır.

            7
           / \
          5   8
         / \   \
        1   6   9
       / \
      0   3

**8.Adım**
Dizinin dokuzuncu elemanı 4; 7'den ve 5'den küçük, 1'den ve 3'den büyük olduğu için 3'ün sağına yazılır.

            7
           / \
          5   8
         / \   \
        1   6   9
       / \
      0   3
           \
            4

**9.Adım**
Dizinin onuncu elemanı 2; 7'den ve 5'den küçük ve 1'den büyük olduğu için subtree 1'in soluna yazılır ve subtree 3'ün soluna yazılır.

            7
           / \
          5   8
         / \   \
        1   6   9
       / \
      0   3
         / \
        2   4


