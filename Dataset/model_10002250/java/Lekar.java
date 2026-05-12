





import java.util.List;
import java.util.ArrayList;

public class Lekar  {

    private String ImeZap;
    private String BrTelZap;
    private String AdrZap;
    private String PrzZap;
    private String Fakultet;
    private String DatZavSk;
    private String Zaposleni_ID;
    private int RadStaz;



    public Lekar(
        String ImeZap,        String BrTelZap,        String AdrZap,        String PrzZap,        String Fakultet,        String DatZavSk,        String Zaposleni_ID,        int RadStaz    ) {
        this.ImeZap = ImeZap;
        this.BrTelZap = BrTelZap;
        this.AdrZap = AdrZap;
        this.PrzZap = PrzZap;
        this.Fakultet = Fakultet;
        this.DatZavSk = DatZavSk;
        this.Zaposleni_ID = Zaposleni_ID;
        this.RadStaz = RadStaz;
    }


    public String getImezap() {
        return ImeZap;
    }

    public void setImezap(String ImeZap) {
        this.ImeZap = ImeZap;
    }
    public String getBrtelzap() {
        return BrTelZap;
    }

    public void setBrtelzap(String BrTelZap) {
        this.BrTelZap = BrTelZap;
    }
    public String getAdrzap() {
        return AdrZap;
    }

    public void setAdrzap(String AdrZap) {
        this.AdrZap = AdrZap;
    }
    public String getPrzzap() {
        return PrzZap;
    }

    public void setPrzzap(String PrzZap) {
        this.PrzZap = PrzZap;
    }
    public String getFakultet() {
        return Fakultet;
    }

    public void setFakultet(String Fakultet) {
        this.Fakultet = Fakultet;
    }
    public String getDatzavsk() {
        return DatZavSk;
    }

    public void setDatzavsk(String DatZavSk) {
        this.DatZavSk = DatZavSk;
    }
    public String getZaposleni_id() {
        return Zaposleni_ID;
    }

    public void setZaposleni_id(String Zaposleni_ID) {
        this.Zaposleni_ID = Zaposleni_ID;
    }
    public int getRadstaz() {
        return RadStaz;
    }

    public void setRadstaz(int RadStaz) {
        this.RadStaz = RadStaz;
    }


}