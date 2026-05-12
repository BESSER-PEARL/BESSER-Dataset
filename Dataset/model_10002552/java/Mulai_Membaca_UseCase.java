





import java.util.List;
import java.util.ArrayList;

public class Mulai_Membaca_UseCase  {






    private Memilih_Kategori_Buku_UseCase memilih_kategori_buku_usecase;


    public Mulai_Membaca_UseCase(
    ) {
    }



    public Memilih_Kategori_Buku_UseCase getMemilih_kategori_buku_usecase() {
        return memilih_kategori_buku_usecase;
    }

    public void setMemilih_kategori_buku_usecase(Memilih_Kategori_Buku_UseCase memilih_kategori_buku_usecase) {
        this.memilih_kategori_buku_usecase = memilih_kategori_buku_usecase;
    }

}