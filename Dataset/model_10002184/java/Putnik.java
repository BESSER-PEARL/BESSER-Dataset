





import java.util.List;
import java.util.ArrayList;

public class Putnik  {

    private int AranzmanID;
    private String PrezimePutnika;
    private String AdresaPutnika;
    private String KontaktPutnika;
    private String GradPutnika;
    private String JMBG;
    private int PutnikID;
    private int BrojPasosa;
    private String ImePutnika;



    public Putnik(
        int AranzmanID,        String PrezimePutnika,        String AdresaPutnika,        String KontaktPutnika,        String GradPutnika,        String JMBG,        int PutnikID,        int BrojPasosa,        String ImePutnika    ) {
        this.AranzmanID = AranzmanID;
        this.PrezimePutnika = PrezimePutnika;
        this.AdresaPutnika = AdresaPutnika;
        this.KontaktPutnika = KontaktPutnika;
        this.GradPutnika = GradPutnika;
        this.JMBG = JMBG;
        this.PutnikID = PutnikID;
        this.BrojPasosa = BrojPasosa;
        this.ImePutnika = ImePutnika;
    }


    public int getAranzmanid() {
        return AranzmanID;
    }

    public void setAranzmanid(int AranzmanID) {
        this.AranzmanID = AranzmanID;
    }
    public String getPrezimeputnika() {
        return PrezimePutnika;
    }

    public void setPrezimeputnika(String PrezimePutnika) {
        this.PrezimePutnika = PrezimePutnika;
    }
    public String getAdresaputnika() {
        return AdresaPutnika;
    }

    public void setAdresaputnika(String AdresaPutnika) {
        this.AdresaPutnika = AdresaPutnika;
    }
    public String getKontaktputnika() {
        return KontaktPutnika;
    }

    public void setKontaktputnika(String KontaktPutnika) {
        this.KontaktPutnika = KontaktPutnika;
    }
    public String getGradputnika() {
        return GradPutnika;
    }

    public void setGradputnika(String GradPutnika) {
        this.GradPutnika = GradPutnika;
    }
    public String getJmbg() {
        return JMBG;
    }

    public void setJmbg(String JMBG) {
        this.JMBG = JMBG;
    }
    public int getPutnikid() {
        return PutnikID;
    }

    public void setPutnikid(int PutnikID) {
        this.PutnikID = PutnikID;
    }
    public int getBrojpasosa() {
        return BrojPasosa;
    }

    public void setBrojpasosa(int BrojPasosa) {
        this.BrojPasosa = BrojPasosa;
    }
    public String getImeputnika() {
        return ImePutnika;
    }

    public void setImeputnika(String ImePutnika) {
        this.ImePutnika = ImePutnika;
    }


}