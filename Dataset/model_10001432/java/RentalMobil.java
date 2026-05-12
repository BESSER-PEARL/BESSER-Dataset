





import java.util.List;
import java.util.ArrayList;

public class RentalMobil  {

    private String Alamat;
    private String Email;
    private String Telepon;
    private String Nama;



    public RentalMobil(
        String Alamat,        String Email,        String Telepon,        String Nama    ) {
        this.Alamat = Alamat;
        this.Email = Email;
        this.Telepon = Telepon;
        this.Nama = Nama;
    }


    public String getAlamat() {
        return Alamat;
    }

    public void setAlamat(String Alamat) {
        this.Alamat = Alamat;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getTelepon() {
        return Telepon;
    }

    public void setTelepon(String Telepon) {
        this.Telepon = Telepon;
    }
    public String getNama() {
        return Nama;
    }

    public void setNama(String Nama) {
        this.Nama = Nama;
    }


}