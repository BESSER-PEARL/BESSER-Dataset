





import java.util.List;
import java.util.ArrayList;

public class user  {

    private String nama_lengkap;
    private int id_user;
    private String asal_sekolah;
    private String instagram;
    private String no_telp;
    private String password;
    private String asal_kota;
    private String email;
    private String gambar;
    private String jenis_kelamin;



    public user(
        String nama_lengkap,        int id_user,        String asal_sekolah,        String instagram,        String no_telp,        String password,        String asal_kota,        String email,        String gambar,        String jenis_kelamin    ) {
        this.nama_lengkap = nama_lengkap;
        this.id_user = id_user;
        this.asal_sekolah = asal_sekolah;
        this.instagram = instagram;
        this.no_telp = no_telp;
        this.password = password;
        this.asal_kota = asal_kota;
        this.email = email;
        this.gambar = gambar;
        this.jenis_kelamin = jenis_kelamin;
    }


    public String getNama_lengkap() {
        return nama_lengkap;
    }

    public void setNama_lengkap(String nama_lengkap) {
        this.nama_lengkap = nama_lengkap;
    }
    public int getId_user() {
        return id_user;
    }

    public void setId_user(int id_user) {
        this.id_user = id_user;
    }
    public String getAsal_sekolah() {
        return asal_sekolah;
    }

    public void setAsal_sekolah(String asal_sekolah) {
        this.asal_sekolah = asal_sekolah;
    }
    public String getInstagram() {
        return instagram;
    }

    public void setInstagram(String instagram) {
        this.instagram = instagram;
    }
    public String getNo_telp() {
        return no_telp;
    }

    public void setNo_telp(String no_telp) {
        this.no_telp = no_telp;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAsal_kota() {
        return asal_kota;
    }

    public void setAsal_kota(String asal_kota) {
        this.asal_kota = asal_kota;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getGambar() {
        return gambar;
    }

    public void setGambar(String gambar) {
        this.gambar = gambar;
    }
    public String getJenis_kelamin() {
        return jenis_kelamin;
    }

    public void setJenis_kelamin(String jenis_kelamin) {
        this.jenis_kelamin = jenis_kelamin;
    }


}