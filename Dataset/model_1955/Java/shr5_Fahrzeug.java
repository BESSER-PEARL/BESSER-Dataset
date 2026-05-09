





import java.util.List;
import java.util.ArrayList;

public class shr5_Fahrzeug extends Capacity, Anwendbar, Modifizierbar, Quelle, GeldWert, Beschreibbar, FahrzeugZustand {

    private String fahrzeugTyp;
    private int pilot;
    private int beschleunigung;
    private int handling;
    private int geschwindigkeit;
    private int rumpf;
    private int panzer;
    private int weaponMounts;
    private int sensor;



    public shr5_Fahrzeug(
        String fahrzeugTyp,        int pilot,        int beschleunigung,        int handling,        int geschwindigkeit,        int rumpf,        int panzer,        int weaponMounts,        int sensor    ) {
        super(
        );
        this.fahrzeugTyp = fahrzeugTyp;
        this.pilot = pilot;
        this.beschleunigung = beschleunigung;
        this.handling = handling;
        this.geschwindigkeit = geschwindigkeit;
        this.rumpf = rumpf;
        this.panzer = panzer;
        this.weaponMounts = weaponMounts;
        this.sensor = sensor;
    }


    public String getFahrzeugtyp() {
        return fahrzeugTyp;
    }

    public void setFahrzeugtyp(String fahrzeugTyp) {
        this.fahrzeugTyp = fahrzeugTyp;
    }
    public int getPilot() {
        return pilot;
    }

    public void setPilot(int pilot) {
        this.pilot = pilot;
    }
    public int getBeschleunigung() {
        return beschleunigung;
    }

    public void setBeschleunigung(int beschleunigung) {
        this.beschleunigung = beschleunigung;
    }
    public int getHandling() {
        return handling;
    }

    public void setHandling(int handling) {
        this.handling = handling;
    }
    public int getGeschwindigkeit() {
        return geschwindigkeit;
    }

    public void setGeschwindigkeit(int geschwindigkeit) {
        this.geschwindigkeit = geschwindigkeit;
    }
    public int getRumpf() {
        return rumpf;
    }

    public void setRumpf(int rumpf) {
        this.rumpf = rumpf;
    }
    public int getPanzer() {
        return panzer;
    }

    public void setPanzer(int panzer) {
        this.panzer = panzer;
    }
    public int getWeaponmounts() {
        return weaponMounts;
    }

    public void setWeaponmounts(int weaponMounts) {
        this.weaponMounts = weaponMounts;
    }
    public int getSensor() {
        return sensor;
    }

    public void setSensor(int sensor) {
        this.sensor = sensor;
    }


}