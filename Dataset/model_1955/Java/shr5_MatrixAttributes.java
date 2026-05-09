





import java.util.List;
import java.util.ArrayList;

public class shr5_MatrixAttributes extends MatixConditionMonitor {

    private int firewall;
    private int geraetestufe;
    private String currentModus;
    private int datenverarbeitung;



    public shr5_MatrixAttributes(
        int firewall,        int geraetestufe,        String currentModus,        int datenverarbeitung    ) {
        super(
        );
        this.firewall = firewall;
        this.geraetestufe = geraetestufe;
        this.currentModus = currentModus;
        this.datenverarbeitung = datenverarbeitung;
    }


    public int getFirewall() {
        return firewall;
    }

    public void setFirewall(int firewall) {
        this.firewall = firewall;
    }
    public int getGeraetestufe() {
        return geraetestufe;
    }

    public void setGeraetestufe(int geraetestufe) {
        this.geraetestufe = geraetestufe;
    }
    public String getCurrentmodus() {
        return currentModus;
    }

    public void setCurrentmodus(String currentModus) {
        this.currentModus = currentModus;
    }
    public int getDatenverarbeitung() {
        return datenverarbeitung;
    }

    public void setDatenverarbeitung(int datenverarbeitung) {
        this.datenverarbeitung = datenverarbeitung;
    }


}