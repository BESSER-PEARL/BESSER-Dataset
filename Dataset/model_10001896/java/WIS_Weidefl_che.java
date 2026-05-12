





import java.util.List;
import java.util.ArrayList;

public class WIS_Weidefl_che  {

    private String name;
    private String farbe;
    private String schlagnummer;
    private int groesse;



    public WIS_Weidefl_che(
        String name,        String farbe,        String schlagnummer,        int groesse    ) {
        this.name = name;
        this.farbe = farbe;
        this.schlagnummer = schlagnummer;
        this.groesse = groesse;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFarbe() {
        return farbe;
    }

    public void setFarbe(String farbe) {
        this.farbe = farbe;
    }
    public String getSchlagnummer() {
        return schlagnummer;
    }

    public void setSchlagnummer(String schlagnummer) {
        this.schlagnummer = schlagnummer;
    }
    public int getGroesse() {
        return groesse;
    }

    public void setGroesse(int groesse) {
        this.groesse = groesse;
    }


}