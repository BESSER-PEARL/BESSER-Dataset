





import java.util.List;
import java.util.ArrayList;

public class Korisnik_IS  {

    private String UserName;
    private String PrezimeKorisnika;
    private String Password;
    private String ImeKorisnika;
    private int KorisnikID;



    public Korisnik_IS(
        String UserName,        String PrezimeKorisnika,        String Password,        String ImeKorisnika,        int KorisnikID    ) {
        this.UserName = UserName;
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.Password = Password;
        this.ImeKorisnika = ImeKorisnika;
        this.KorisnikID = KorisnikID;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPrezimekorisnika() {
        return PrezimeKorisnika;
    }

    public void setPrezimekorisnika(String PrezimeKorisnika) {
        this.PrezimeKorisnika = PrezimeKorisnika;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getImekorisnika() {
        return ImeKorisnika;
    }

    public void setImekorisnika(String ImeKorisnika) {
        this.ImeKorisnika = ImeKorisnika;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }


}