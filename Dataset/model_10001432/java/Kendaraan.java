





import java.util.List;
import java.util.ArrayList;

public class Kendaraan  {

    private String Warna;
    private String TahunPembuatan;
    private String NoMesin;
    private String NoRangka;
    private String Merk;
    private String NoPolisi;





    private Pesan pesan;




    private Pelanggan pelanggan;


    public Kendaraan(
        String Warna,        String TahunPembuatan,        String NoMesin,        String NoRangka,        String Merk,        String NoPolisi    ) {
        this.Warna = Warna;
        this.TahunPembuatan = TahunPembuatan;
        this.NoMesin = NoMesin;
        this.NoRangka = NoRangka;
        this.Merk = Merk;
        this.NoPolisi = NoPolisi;
    }


    public String getWarna() {
        return Warna;
    }

    public void setWarna(String Warna) {
        this.Warna = Warna;
    }
    public String getTahunpembuatan() {
        return TahunPembuatan;
    }

    public void setTahunpembuatan(String TahunPembuatan) {
        this.TahunPembuatan = TahunPembuatan;
    }
    public String getNomesin() {
        return NoMesin;
    }

    public void setNomesin(String NoMesin) {
        this.NoMesin = NoMesin;
    }
    public String getNorangka() {
        return NoRangka;
    }

    public void setNorangka(String NoRangka) {
        this.NoRangka = NoRangka;
    }
    public String getMerk() {
        return Merk;
    }

    public void setMerk(String Merk) {
        this.Merk = Merk;
    }
    public String getNopolisi() {
        return NoPolisi;
    }

    public void setNopolisi(String NoPolisi) {
        this.NoPolisi = NoPolisi;
    }

    public Pesan getPesan() {
        return pesan;
    }

    public void setPesan(Pesan pesan) {
        this.pesan = pesan;
    }
    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public void setPelanggan(Pelanggan pelanggan) {
        this.pelanggan = pelanggan;
    }

}