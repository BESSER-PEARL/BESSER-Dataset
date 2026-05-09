





import java.util.List;
import java.util.ArrayList;

public class shr5_Sprite extends Quelle, Beschreibbar, ResonanzPersona {

    private int datenverarbeitungMod;
    private int firewallMod;
    private int initativeMod;
    private int schleicherMod;
    private int stufe;
    private int angriffMod;



    public shr5_Sprite(
        int datenverarbeitungMod,        int firewallMod,        int initativeMod,        int schleicherMod,        int stufe,        int angriffMod    ) {
        super(
        );
        this.datenverarbeitungMod = datenverarbeitungMod;
        this.firewallMod = firewallMod;
        this.initativeMod = initativeMod;
        this.schleicherMod = schleicherMod;
        this.stufe = stufe;
        this.angriffMod = angriffMod;
    }


    public int getDatenverarbeitungmod() {
        return datenverarbeitungMod;
    }

    public void setDatenverarbeitungmod(int datenverarbeitungMod) {
        this.datenverarbeitungMod = datenverarbeitungMod;
    }
    public int getFirewallmod() {
        return firewallMod;
    }

    public void setFirewallmod(int firewallMod) {
        this.firewallMod = firewallMod;
    }
    public int getInitativemod() {
        return initativeMod;
    }

    public void setInitativemod(int initativeMod) {
        this.initativeMod = initativeMod;
    }
    public int getSchleichermod() {
        return schleicherMod;
    }

    public void setSchleichermod(int schleicherMod) {
        this.schleicherMod = schleicherMod;
    }
    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }
    public int getAngriffmod() {
        return angriffMod;
    }

    public void setAngriffmod(int angriffMod) {
        this.angriffMod = angriffMod;
    }


}