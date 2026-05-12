





import java.util.List;
import java.util.ArrayList;

public class Korisnik_IS  {

    private String UserName;
    private String Password;
    private String ImeKorisnika;
    private String PrezimeKorisnika;
    private int KorisnikID;





    private List<Rezervisanje> rezervisanjes;


    public Korisnik_IS(
        String UserName,        String Password,        String ImeKorisnika,        String PrezimeKorisnika,        int KorisnikID    ) {
        this.UserName = UserName;
        this.Password = Password;
        this.ImeKorisnika = ImeKorisnika;
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.KorisnikID = KorisnikID;
        this.rezervisanjes = new ArrayList<>();
    }

    public Korisnik_IS(
        String UserName,        String Password,        String ImeKorisnika,        String PrezimeKorisnika,        int KorisnikID        ArrayList<Rezervisanje> rezervisanjes    ) {
        this.UserName = UserName;
        this.Password = Password;
        this.ImeKorisnika = ImeKorisnika;
        this.PrezimeKorisnika = PrezimeKorisnika;
        this.KorisnikID = KorisnikID;
        this.rezervisanjes = rezervisanjes;
    }

    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
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

    public List<Rezervisanje> getRezervisanjes() {
        return rezervisanjes;
    }

    public void addRezervisanje(Rezervisanje rezervisanje) {
        this.rezervisanjes.add(rezervisanje);
    }

}