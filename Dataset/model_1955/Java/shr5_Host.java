





import java.util.List;
import java.util.ArrayList;

public class shr5_Host extends Beschreibbar, ActiveMatixDevice, MatrixDevice {

    private int hostRating;
    private int baseDatenverarbeitung;
    private int baseSchleicher;
    private int baseFirewall;
    private int baseAngriff;



    public shr5_Host(
        int hostRating,        int baseDatenverarbeitung,        int baseSchleicher,        int baseFirewall,        int baseAngriff    ) {
        super(
        );
        this.hostRating = hostRating;
        this.baseDatenverarbeitung = baseDatenverarbeitung;
        this.baseSchleicher = baseSchleicher;
        this.baseFirewall = baseFirewall;
        this.baseAngriff = baseAngriff;
    }


    public int getHostrating() {
        return hostRating;
    }

    public void setHostrating(int hostRating) {
        this.hostRating = hostRating;
    }
    public int getBasedatenverarbeitung() {
        return baseDatenverarbeitung;
    }

    public void setBasedatenverarbeitung(int baseDatenverarbeitung) {
        this.baseDatenverarbeitung = baseDatenverarbeitung;
    }
    public int getBaseschleicher() {
        return baseSchleicher;
    }

    public void setBaseschleicher(int baseSchleicher) {
        this.baseSchleicher = baseSchleicher;
    }
    public int getBasefirewall() {
        return baseFirewall;
    }

    public void setBasefirewall(int baseFirewall) {
        this.baseFirewall = baseFirewall;
    }
    public int getBaseangriff() {
        return baseAngriff;
    }

    public void setBaseangriff(int baseAngriff) {
        this.baseAngriff = baseAngriff;
    }


}