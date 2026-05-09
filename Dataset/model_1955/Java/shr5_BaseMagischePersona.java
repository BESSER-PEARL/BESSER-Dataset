





import java.util.List;
import java.util.ArrayList;

public class shr5_BaseMagischePersona  {

    private int magie;
    private int magieBasis;





    private List<shr5_Initation> shr5_initations;


    public shr5_BaseMagischePersona(
        int magie,        int magieBasis    ) {
        this.magie = magie;
        this.magieBasis = magieBasis;
        this.shr5_initations = new ArrayList<>();
    }

    public shr5_BaseMagischePersona(
        int magie,        int magieBasis        ArrayList<shr5_Initation> shr5_initations    ) {
        this.magie = magie;
        this.magieBasis = magieBasis;
        this.shr5_initations = shr5_initations;
    }

    public int getMagie() {
        return magie;
    }

    public void setMagie(int magie) {
        this.magie = magie;
    }
    public int getMagiebasis() {
        return magieBasis;
    }

    public void setMagiebasis(int magieBasis) {
        this.magieBasis = magieBasis;
    }

    public List<shr5_Initation> getShr5_initations() {
        return shr5_initations;
    }

    public void addShr5_initation(Shr5_initation shr5_initation) {
        this.shr5_initations.add(shr5_initation);
    }

}