





import java.util.List;
import java.util.ArrayList;

public class shr5_KomplexeForm extends Quelle, Beschreibbar {

    private String ziel;
    private String dauer;
    private String schwund;



    public shr5_KomplexeForm(
        String ziel,        String dauer,        String schwund    ) {
        super(
        );
        this.ziel = ziel;
        this.dauer = dauer;
        this.schwund = schwund;
    }


    public String getZiel() {
        return ziel;
    }

    public void setZiel(String ziel) {
        this.ziel = ziel;
    }
    public String getDauer() {
        return dauer;
    }

    public void setDauer(String dauer) {
        this.dauer = dauer;
    }
    public String getSchwund() {
        return schwund;
    }

    public void setSchwund(String schwund) {
        this.schwund = schwund;
    }


}