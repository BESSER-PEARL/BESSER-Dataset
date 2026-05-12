





import java.util.List;
import java.util.ArrayList;

public class Kupac  {

    private int Mobilni;
    private String Grad;
    private int BrojPasosa;
    private String Prezime;
    private int JMBG;
    private String Ime;
    private String Kupac_ID;





    private Osiguranje osiguranje;




    private Agent agent;




    private List<Aran_man> aran_mans;


    public Kupac(
        int Mobilni,        String Grad,        int BrojPasosa,        String Prezime,        int JMBG,        String Ime,        String Kupac_ID    ) {
        this.Mobilni = Mobilni;
        this.Grad = Grad;
        this.BrojPasosa = BrojPasosa;
        this.Prezime = Prezime;
        this.JMBG = JMBG;
        this.Ime = Ime;
        this.Kupac_ID = Kupac_ID;
        this.aran_mans = new ArrayList<>();
    }

    public Kupac(
        int Mobilni,        String Grad,        int BrojPasosa,        String Prezime,        int JMBG,        String Ime,        String Kupac_ID        ArrayList<Aran_man> aran_mans    ) {
        this.Mobilni = Mobilni;
        this.Grad = Grad;
        this.BrojPasosa = BrojPasosa;
        this.Prezime = Prezime;
        this.JMBG = JMBG;
        this.Ime = Ime;
        this.Kupac_ID = Kupac_ID;
        this.aran_mans = aran_mans;
    }

    public int getMobilni() {
        return Mobilni;
    }

    public void setMobilni(int Mobilni) {
        this.Mobilni = Mobilni;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public int getBrojpasosa() {
        return BrojPasosa;
    }

    public void setBrojpasosa(int BrojPasosa) {
        this.BrojPasosa = BrojPasosa;
    }
    public String getPrezime() {
        return Prezime;
    }

    public void setPrezime(String Prezime) {
        this.Prezime = Prezime;
    }
    public int getJmbg() {
        return JMBG;
    }

    public void setJmbg(int JMBG) {
        this.JMBG = JMBG;
    }
    public String getIme() {
        return Ime;
    }

    public void setIme(String Ime) {
        this.Ime = Ime;
    }
    public String getKupac_id() {
        return Kupac_ID;
    }

    public void setKupac_id(String Kupac_ID) {
        this.Kupac_ID = Kupac_ID;
    }

    public Osiguranje getOsiguranje() {
        return osiguranje;
    }

    public void setOsiguranje(Osiguranje osiguranje) {
        this.osiguranje = osiguranje;
    }
    public Agent getAgent() {
        return agent;
    }

    public void setAgent(Agent agent) {
        this.agent = agent;
    }
    public List<Aran_man> getAran_mans() {
        return aran_mans;
    }

    public void addAran_man(Aran_man aran_man) {
        this.aran_mans.add(aran_man);
    }

}