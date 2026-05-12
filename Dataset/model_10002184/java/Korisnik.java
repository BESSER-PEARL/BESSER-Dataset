





import java.util.List;
import java.util.ArrayList;

public class Korisnik  {

    private String AdresaKorisnika;
    private String ImeKorisnika;
    private String JMBG;
    private int KorisnikID;
    private String KontaktKorisnika;
    private String Password;
    private String Username;
    private String GradKorisnika;
    private String PrezimeKorisnika;



    public Korisnik(
        String AdresaKorisnika,        String ImeKorisnika,        String JMBG,        int KorisnikID,        String KontaktKorisnika,        String Password,        String Username,        String GradKorisnika,        String PrezimeKorisnika    ) {
        this.AdresaKorisnika = AdresaKorisnika;
        this.ImeKorisnika = ImeKorisnika;
        this.JMBG = JMBG;
        this.KorisnikID = KorisnikID;
        this.KontaktKorisnika = KontaktKorisnika;
        this.Password = Password;
        this.Username = Username;
        this.GradKorisnika = GradKorisnika;
        this.PrezimeKorisnika = PrezimeKorisnika;
    }


    public String getAdresakorisnika() {
        return AdresaKorisnika;
    }

    public void setAdresakorisnika(String AdresaKorisnika) {
        this.AdresaKorisnika = AdresaKorisnika;
    }
    public String getImekorisnika() {
        return ImeKorisnika;
    }

    public void setImekorisnika(String ImeKorisnika) {
        this.ImeKorisnika = ImeKorisnika;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }
    public String getKontaktkorisnika() {
        return KontaktKorisnika;
    }

    public void setKontaktkorisnika(String KontaktKorisnika) {
        this.KontaktKorisnika = KontaktKorisnika;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getGradkorisnika() {
        return GradKorisnika;
    }

    public void setGradkorisnika(String GradKorisnika) {
        this.GradKorisnika = GradKorisnika;
    }
    public String getPrezimekorisnika() {
        return PrezimeKorisnika;
    }

    public void setPrezimekorisnika(String PrezimeKorisnika) {
        this.PrezimeKorisnika = PrezimeKorisnika;
    }


}