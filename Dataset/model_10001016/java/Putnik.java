





import java.util.List;
import java.util.ArrayList;

public class Putnik  {

    private int PutnikID;
    private String ImePut;
    private String Adresa;
    private int OsigID;
    private int Mobilni;
    private String eMail;
    private String PrezimePut;
    private String Grad;
    private String JMBG;





    private List<Rezervisanje> rezervisanjes;




    private Osiguranje osiguranje;


    public Putnik(
        int PutnikID,        String ImePut,        String Adresa,        int OsigID,        int Mobilni,        String eMail,        String PrezimePut,        String Grad,        String JMBG    ) {
        this.PutnikID = PutnikID;
        this.ImePut = ImePut;
        this.Adresa = Adresa;
        this.OsigID = OsigID;
        this.Mobilni = Mobilni;
        this.eMail = eMail;
        this.PrezimePut = PrezimePut;
        this.Grad = Grad;
        this.JMBG = JMBG;
        this.rezervisanjes = new ArrayList<>();
    }

    public Putnik(
        int PutnikID,        String ImePut,        String Adresa,        int OsigID,        int Mobilni,        String eMail,        String PrezimePut,        String Grad,        String JMBG        ArrayList<Rezervisanje> rezervisanjes    ) {
        this.PutnikID = PutnikID;
        this.ImePut = ImePut;
        this.Adresa = Adresa;
        this.OsigID = OsigID;
        this.Mobilni = Mobilni;
        this.eMail = eMail;
        this.PrezimePut = PrezimePut;
        this.Grad = Grad;
        this.JMBG = JMBG;
        this.rezervisanjes = rezervisanjes;
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
    public String getAdresa() {
        return Adresa;
    }

    public void setAdresa(String Adresa) {
        this.Adresa = Adresa;
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
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
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