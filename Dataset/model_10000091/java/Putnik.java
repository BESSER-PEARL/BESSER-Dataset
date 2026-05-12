





import java.util.List;
import java.util.ArrayList;

public class Putnik  {

    private String eMail;
    private String PrezimePut;
    private String JMBG;
    private String Grad;
    private int PutnikID;
    private String ImePut;
    private int OsigID;
    private int Mobilni;
    private String Adresa;





    private Osiguranje osiguranje;




    private List<Rezervisanje> rezervisanjes;


    public Putnik(
        String eMail,        String PrezimePut,        String JMBG,        String Grad,        int PutnikID,        String ImePut,        int OsigID,        int Mobilni,        String Adresa    ) {
        this.eMail = eMail;
        this.PrezimePut = PrezimePut;
        this.JMBG = JMBG;
        this.Grad = Grad;
        this.PutnikID = PutnikID;
        this.ImePut = ImePut;
        this.OsigID = OsigID;
        this.Mobilni = Mobilni;
        this.Adresa = Adresa;
        this.rezervisanjes = new ArrayList<>();
    }

    public Putnik(
        String eMail,        String PrezimePut,        String JMBG,        String Grad,        int PutnikID,        String ImePut,        int OsigID,        int Mobilni,        String Adresa        ArrayList<Rezervisanje> rezervisanjes    ) {
        this.eMail = eMail;
        this.PrezimePut = PrezimePut;
        this.JMBG = JMBG;
        this.Grad = Grad;
        this.PutnikID = PutnikID;
        this.ImePut = ImePut;
        this.OsigID = OsigID;
        this.Mobilni = Mobilni;
        this.Adresa = Adresa;
        this.rezervisanjes = rezervisanjes;
    }

    public String getEmail() {
        return eMail;
    }

    public void setEmail(String eMail) {
        this.eMail = eMail;
    }
    public String getPrezimeput() {
        return PrezimePut;
    }

    public void setPrezimeput(String PrezimePut) {
        this.PrezimePut = PrezimePut;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public String getImeput() {
        return ImePut;
    }

    public void setImeput(String ImePut) {
        this.ImePut = ImePut;
    }
    public int getOsigid() {
        return OsigID;
    }

    public void setOsigid(int OsigID) {
        this.OsigID = OsigID;
    }
    public int getMobilni() {
        return Mobilni;
    }

    public void setMobilni(int Mobilni) {
        this.Mobilni = Mobilni;
    }
    public String getAdresa() {
        return Adresa;
    }

    public void setAdresa(String Adresa) {
        this.Adresa = Adresa;
    }

    public Osiguranje getOsiguranje() {
        return osiguranje;
    }

    public void setOsiguranje(Osiguranje osiguranje) {
        this.osiguranje = osiguranje;
    }
    public List<Rezervisanje> getRezervisanjes() {
        return rezervisanjes;
    }

    public void addRezervisanje(Rezervisanje rezervisanje) {
        this.rezervisanjes.add(rezervisanje);
    }

}