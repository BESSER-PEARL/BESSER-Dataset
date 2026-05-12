





import java.util.List;
import java.util.ArrayList;

public class Korisnik_IS  {

    private String PrezimeKorisnika;
    private int KorisnikID;
    private String UserName;
    private String ImeKorisnika;
    private String Password;





    private List<Rezervisanje> rezervisanjes;


    public Korisnik_IS(
        String PrezimeKorisnika,        int KorisnikID,        String UserName,        String ImeKorisnika,        String Password    ) {
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.KorisnikID = KorisnikID;
        this.UserName = UserName;
        this.ImeKorisnika = ImeKorisnika;
        this.Password = Password;
        this.rezervisanjes = new ArrayList<>();
    }

    public Korisnik_IS(
        String PrezimeKorisnika,        int KorisnikID,        String UserName,        String ImeKorisnika,        String Password        ArrayList<Rezervisanje> rezervisanjes    ) {
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.KorisnikID = KorisnikID;
        this.UserName = UserName;
        this.ImeKorisnika = ImeKorisnika;
        this.Password = Password;
        this.rezervisanjes = rezervisanjes;
    }

    public String getPrezimekorisnika() {
        return PrezimeKorisnika;
    }

    public void setPrezimekorisnika(String PrezimeKorisnika) {
        this.PrezimeKorisnika = PrezimeKorisnika;
    }
    public int getKorisnikid() {
        return KorisnikID;
    }

    public void setKorisnikid(int KorisnikID) {
        this.KorisnikID = KorisnikID;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getImekorisnika() {
        return ImeKorisnika;
    }

    public void setImekorisnika(String ImeKorisnika) {
        this.ImeKorisnika = ImeKorisnika;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public List<Rezervisanje> getRezervisanjes() {
        return rezervisanjes;
    }

    public void addRezervisanje(Rezervisanje rezervisanje) {
        this.rezervisanjes.add(rezervisanje);
    }

}