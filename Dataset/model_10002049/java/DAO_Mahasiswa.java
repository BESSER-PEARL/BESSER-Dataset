





import java.util.List;
import java.util.ArrayList;

public class DAO_Mahasiswa  {

    private String tahun;
    private String nim;
    private String nama;





    private Mahasiswa mahasiswa;


    public DAO_Mahasiswa(
        String tahun,        String nim,        String nama    ) {
        this.tahun = tahun;
        this.nim = nim;
        this.nama = nama;
    }


    public String getTahun() {
        return tahun;
    }

    public void setTahun(String tahun) {
        this.tahun = tahun;
    }
    public String getNim() {
        return nim;
    }

    public void setNim(String nim) {
        this.nim = nim;
    }
    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public Mahasiswa getMahasiswa() {
        return mahasiswa;
    }

    public void setMahasiswa(Mahasiswa mahasiswa) {
        this.mahasiswa = mahasiswa;
    }

}