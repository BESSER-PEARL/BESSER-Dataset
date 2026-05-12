





import java.util.List;
import java.util.ArrayList;

public class Putnik  {

    private String BrojTel;
    private int PutnikID;
    private String Adresa;
    private String ImePutnik;
    private String PrezimePutnik;
    private String Grad;
    private String Email;
    private int OsiguranjeID;
    private String JMBG;





    private Rezervacija rezervacija;




    private Osiguranje osiguranje;


    public Putnik(
        String BrojTel,        int PutnikID,        String Adresa,        String ImePutnik,        String PrezimePutnik,        String Grad,        String Email,        int OsiguranjeID,        String JMBG    ) {
        this.BrojTel = BrojTel;
        this.PutnikID = PutnikID;
        this.Adresa = Adresa;
        this.ImePutnik = ImePutnik;
        this.PrezimePutnik = PrezimePutnik;
        this.Grad = Grad;
        this.Email = Email;
        this.OsiguranjeID = OsiguranjeID;
        this.JMBG = JMBG;
    }


    public String getBrojtel() {
        return BrojTel;
    }

    public void setBrojtel(String BrojTel) {
        this.BrojTel = BrojTel;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public String getAdresa() {
        return Adresa;
    }

    public void setAdresa(String Adresa) {
        this.Adresa = Adresa;
    }
    public String getImeputnik() {
        return ImePutnik;
    }

    public void setImeputnik(String ImePutnik) {
        this.ImePutnik = ImePutnik;
    }
    public String getPrezimeputnik() {
        return PrezimePutnik;
    }

    public void setPrezimeputnik(String PrezimePutnik) {
        this.PrezimePutnik = PrezimePutnik;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getOsiguranjeid() {
        return OsiguranjeID;
    }

    public void setOsiguranjeid(int OsiguranjeID) {
        this.OsiguranjeID = OsiguranjeID;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }

    public Rezervacija getRezervacija() {
        return rezervacija;
    }

    public void setRezervacija(Rezervacija rezervacija) {
        this.rezervacija = rezervacija;
    }
    public Osiguranje getOsiguranje() {
        return osiguranje;
    }

    public void setOsiguranje(Osiguranje osiguranje) {
        this.osiguranje = osiguranje;
    }

}