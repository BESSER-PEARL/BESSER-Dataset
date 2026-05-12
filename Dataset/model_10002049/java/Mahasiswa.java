





import java.util.List;
import java.util.ArrayList;

public class Mahasiswa  {

    private String nim;
    private String nama;
    private String tahun;



    public Mahasiswa(
        String nim,        String nama,        String tahun    ) {
        this.nim = nim;
        this.nama = nama;
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
    public String getTahun() {
        return tahun;
    }

    public void setTahun(String tahun) {
        this.tahun = tahun;
    }


}