





import java.util.List;
import java.util.ArrayList;

public class Korisnik_IS  {

    private String PrezimeKorisnika;
    private String UserName;
    private int KorisnikID;
    private String Password;
    private String ImeKorisnika;



    public Korisnik_IS(
        String PrezimeKorisnika,        String UserName,        int KorisnikID,        String Password,        String ImeKorisnika    ) {
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.UserName = UserName;
        this.KorisnikID = KorisnikID;
        this.Password = Password;
        this.ImeKorisnika = ImeKorisnika;
    }


    public String getPrezimekorisnika() {
        return PrezimeKorisnika;
    }

    public void setPrezimekorisnika(String PrezimeKorisnika) {
        this.PrezimeKorisnika = PrezimeKorisnika;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
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


}