





import java.util.List;
import java.util.ArrayList;

public class Zaposlen  {

    private float urnaPostavka;
    private String izobrazba;



    public Zaposlen(
        float urnaPostavka,        String izobrazba    ) {
        this.urnaPostavka = urnaPostavka;
        this.izobrazba = izobrazba;
    }


    public float getUrnapostavka() {
        return urnaPostavka;
    }

    public void setUrnapostavka(float urnaPostavka) {
        this.urnaPostavka = urnaPostavka;
    }
    public String getIzobrazba() {
        return izobrazba;
    }

    public void setIzobrazba(String izobrazba) {
        this.izobrazba = izobrazba;
    }


}