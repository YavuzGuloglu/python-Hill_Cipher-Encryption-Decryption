Python ile Hill Şifreleme

### HİLL ŞİFRELEME
Şifrelerken; ilk olarak metin karakterleri ikili bloklara bölünerek blok blok ayrılır ve bunun üzerinden şifrelenir. Verilen anahtar 
matrisi ile metindeki karakterler alfabede karşılık geldiği değerlerine göre çarpılır. 
Çarpım sonuçları toplanır ve alfabedeki karakter sayısına göre modu alınarak şifreli metin karakterleri elde edilir.

### HİLL ŞİFRE ÇÖZME
Şifreyi çözerken; ilk olarak matrisin determinantı alınır.Matrisin tersi 1/determinant ile çarpılır ve sonuç matrisi oluşturulur. 
Sonrasında sonuç matrisiyle şifreli karakterler çarpılarak şifre çözülür.
