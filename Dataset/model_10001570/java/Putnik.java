





import java.util.List;
import java.util.ArrayList;

public class Putnik  {

    private int Mobilni;
    private int OsigID;
    private String Adresa;
    private String JMBG;
    private String PrezimePut;
    private String ImePut;
    private String eMail;
    private int PutnikID;
    private String Grad;





    private List<Rezervisanje> rezervisanjes;




    private Osiguranje osiguranje;


    public Putnik(
        int Mobilni,        int OsigID,        String Adresa,        String JMBG,        String PrezimePut,        String ImePut,        String eMail,        int PutnikID,        String Grad    ) {
        this.Mobilni = Mobilni;
        this.OsigID = OsigID;
        this.Adresa = Adresa;
        this.JMBG = JMBG;
        this.PrezimePut = PrezimePut;
        this.ImePut = ImePut;
        this.eMail = eMail;
        this.PutnikID = PutnikID;
        this.Grad = Grad;
        this.rezervisanjes = new ArrayList<>();
    }

    public Putnik(
        int Mobilni,        int OsigID,        String Adresa,        String JMBG,        String PrezimePut,        String ImePut,        String eMail,        int PutnikID,        String Grad        ArrayList<Rezervisanje> rezervisanjes    ) {
        this.Mobilni = Mobilni;
        this.OsigID = OsigID;
        this.Adresa = Adresa;
        this.JMBG = JMBG;
        this.PrezimePut = PrezimePut;
        this.ImePut = ImePut;
        this.eMail = eMail;
        this.PutnikID = PutnikID;
        this.Grad = Grad;
        this.rezervisanjes = rezervisanjes;
    }

    public int getMobilni() {
        return Mobilni;
    }

    public void setMobilni(int Mobilni) {
        this.Mobilni = Mobilni;
    }
    public int getOsigid() {
        return OsigID;
    }

    public void setOsigid(int OsigID) {
        this.OsigID = OsigID;
    }
    public String getAdresa() {
        return Adresa;
    }

    public void setAdresa(String Adresa) {
        this.Adresa = Adresa;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public String getPrezimeput() {
        return PrezimePut;
    }

    public void setPrezimeput(String PrezimePut) {
        this.PrezimePut = PrezimePut;
    }
    public String getImeput() {
        return ImePut;
    }

    public void setImeput(String ImePut) {
        this.ImePut = ImePut;
    }
    public String getEmail() {
        return eMail;
    }

    public void setEmail(String eMail) {
        this.eMail = eMail;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }

    public List<Rezervisanje> getRezervisanjes() {
        return rezervisanjes;
    }

    public void addRezervisanje(Rezervisanje rezervisanje) {
        this.rezervisanjes.add(rezervisanje);
    }
    public Osiguranje getOsiguranje() {
        return osiguranje;
    }

    public void setOsiguranje(Osiguranje osiguranje) {
        this.osiguranje = osiguranje;
    }

}