





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Munition extends AbstaktGegenstand {

    private String schadensTyp;
    private int power;
    private int niveau;





    private shadowrun_Reichweite shadowrun_reichweite;


    public shadowrun_Munition(
        String schadensTyp,        int power,        int niveau    ) {
        super(
        );
        this.schadensTyp = schadensTyp;
        this.power = power;
        this.niveau = niveau;
    }


    public String getSchadenstyp() {
        return schadensTyp;
    }

    public void setSchadenstyp(String schadensTyp) {
        this.schadensTyp = schadensTyp;
    }
    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }
    public int getNiveau() {
        return niveau;
    }

    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    public shadowrun_Reichweite getShadowrun_reichweite() {
        return shadowrun_reichweite;
    }

    public void setShadowrun_reichweite(shadowrun_Reichweite shadowrun_reichweite) {
        this.shadowrun_reichweite = shadowrun_reichweite;
    }

}