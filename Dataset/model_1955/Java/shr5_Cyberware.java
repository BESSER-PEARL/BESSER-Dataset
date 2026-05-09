





import java.util.List;
import java.util.ArrayList;

public class shr5_Cyberware extends Capacity, Koerpermods, GeldWert {

    private String type;
    private int cyberwareCapacity;





    private shr5_AbstraktPersona shr5_abstraktpersona;




    private List<shr5_CyberwareEnhancement> shr5_cyberwareenhancements;




    private List<shr5_DefaultWifi> shr5_defaultwifis;


    public shr5_Cyberware(
        String type,        int cyberwareCapacity    ) {
        super(
        );
        this.type = type;
        this.cyberwareCapacity = cyberwareCapacity;
        this.shr5_cyberwareenhancements = new ArrayList<>();
        this.shr5_defaultwifis = new ArrayList<>();
    }

    public shr5_Cyberware(
        String type,        int cyberwareCapacity        ArrayList<shr5_CyberwareEnhancement> shr5_cyberwareenhancements,        ArrayList<shr5_DefaultWifi> shr5_defaultwifis    ) {
        this.type = type;
        this.cyberwareCapacity = cyberwareCapacity;
        this.shr5_cyberwareenhancements = shr5_cyberwareenhancements;
        this.shr5_defaultwifis = shr5_defaultwifis;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getCyberwarecapacity() {
        return cyberwareCapacity;
    }

    public void setCyberwarecapacity(int cyberwareCapacity) {
        this.cyberwareCapacity = cyberwareCapacity;
    }

    public shr5_AbstraktPersona getShr5_abstraktpersona() {
        return shr5_abstraktpersona;
    }

    public void setShr5_abstraktpersona(shr5_AbstraktPersona shr5_abstraktpersona) {
        this.shr5_abstraktpersona = shr5_abstraktpersona;
    }
    public List<shr5_CyberwareEnhancement> getShr5_cyberwareenhancements() {
        return shr5_cyberwareenhancements;
    }

    public void addShr5_cyberwareenhancement(Shr5_cyberwareenhancement shr5_cyberwareenhancement) {
        this.shr5_cyberwareenhancements.add(shr5_cyberwareenhancement);
    }
    public List<shr5_DefaultWifi> getShr5_defaultwifis() {
        return shr5_defaultwifis;
    }

    public void addShr5_defaultwifi(Shr5_defaultwifi shr5_defaultwifi) {
        this.shr5_defaultwifis.add(shr5_defaultwifi);
    }

}