





import java.util.List;
import java.util.ArrayList;

public class shr5_MagischeTradition extends Quelle, Beschreibbar {

    private String enzug;





    private List<shr5_Geist> shr5_geists;




    private shr5_Zauberer shr5_zauberer;


    public shr5_MagischeTradition(
        String enzug    ) {
        super(
        );
        this.enzug = enzug;
        this.shr5_geists = new ArrayList<>();
    }

    public shr5_MagischeTradition(
        String enzug        ArrayList<shr5_Geist> shr5_geists    ) {
        this.enzug = enzug;
        this.shr5_geists = shr5_geists;
    }

    public String getEnzug() {
        return enzug;
    }

    public void setEnzug(String enzug) {
        this.enzug = enzug;
    }

    public List<shr5_Geist> getShr5_geists() {
        return shr5_geists;
    }

    public void addShr5_geist(Shr5_geist shr5_geist) {
        this.shr5_geists.add(shr5_geist);
    }
    public shr5_Zauberer getShr5_zauberer() {
        return shr5_zauberer;
    }

    public void setShr5_zauberer(shr5_Zauberer shr5_zauberer) {
        this.shr5_zauberer = shr5_zauberer;
    }

}