





import java.util.List;
import java.util.ArrayList;

public class Kupac  {

    private String Adresa;
    private String Grad;
    private int OsigID;
    private String ImeKup;
    private int KupacID;
    private String PrezimeKup;
    private String eMail;
    private String JMBG;
    private int Mobilni;





    private List<Aran_man> aran_mans;




    private Osiguranje osiguranje;


    public Kupac(
        String Adresa,        String Grad,        int OsigID,        String ImeKup,        int KupacID,        String PrezimeKup,        String eMail,        String JMBG,        int Mobilni    ) {
        this.Adresa = Adresa;
        this.Grad = Grad;
        this.OsigID = OsigID;
        this.ImeKup = ImeKup;
        this.KupacID = KupacID;
        this.PrezimeKup = PrezimeKup;
        this.eMail = eMail;
        this.JMBG = JMBG;
        this.Mobilni = Mobilni;
        this.aran_mans = new ArrayList<>();
    }

    public Kupac(
        String Adresa,        String Grad,        int OsigID,        String ImeKup,        int KupacID,        String PrezimeKup,        String eMail,        String JMBG,        int Mobilni        ArrayList<Aran_man> aran_mans    ) {
        this.Adresa = Adresa;
        this.Grad = Grad;
        this.OsigID = OsigID;
        this.ImeKup = ImeKup;
        this.KupacID = KupacID;
        this.PrezimeKup = PrezimeKup;
        this.eMail = eMail;
        this.JMBG = JMBG;
        this.Mobilni = Mobilni;
        this.aran_mans = aran_mans;
    }

    public String getAdresa() {
        return Adresa;
    }

    public void setAdresa(String Adresa) {
        this.Adresa = Adresa;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public int getOsigid() {
        return OsigID;
    }

    public void setOsigid(int OsigID) {
        this.OsigID = OsigID;
    }
    public String getImekup() {
        return ImeKup;
    }

    public void setImekup(String ImeKup) {
        this.ImeKup = ImeKup;
    }
    public int getKupacid() {
        return KupacID;
    }

    public void setKupacid(int KupacID) {
        this.KupacID = KupacID;
    }
    public String getPrezimekup() {
        return PrezimeKup;
    }

    public void setPrezimekup(String PrezimeKup) {
        this.PrezimeKup = PrezimeKup;
    }
    public String getEmail() {
        return eMail;
    }

    public void setEmail(String eMail) {
        this.eMail = eMail;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public int getMobilni() {
        return Mobilni;
    }

    public void setMobilni(int Mobilni) {
        this.Mobilni = Mobilni;
    }

    public List<Aran_man> getAran_mans() {
        return aran_mans;
    }

    public void addAran_man(Aran_man aran_man) {
        this.aran_mans.add(aran_man);
    }
    public Osiguranje getOsiguranje() {
        return osiguranje;
    }

    public void setOsiguranje(Osiguranje osiguranje) {
        this.osiguranje = osiguranje;
    }

}