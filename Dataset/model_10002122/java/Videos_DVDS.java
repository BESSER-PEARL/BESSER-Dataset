





import java.util.List;
import java.util.ArrayList;

public class Videos_DVDS  {

    private int Laufzeit;
    private String entLeihungsGeb_hr;
    private int AnzahlEntlehnungen;
    private String Regisseur;



    public Videos_DVDS(
        int Laufzeit,        String entLeihungsGeb_hr,        int AnzahlEntlehnungen,        String Regisseur    ) {
        this.Laufzeit = Laufzeit;
        this.entLeihungsGeb_hr = entLeihungsGeb_hr;
        this.AnzahlEntlehnungen = AnzahlEntlehnungen;
        this.Regisseur = Regisseur;
    }


    public int getLaufzeit() {
        return Laufzeit;
    }

    public void setLaufzeit(int Laufzeit) {
        this.Laufzeit = Laufzeit;
    }
    public String getEntleihungsgeb_hr() {
        return entLeihungsGeb_hr;
    }

    public void setEntleihungsgeb_hr(String entLeihungsGeb_hr) {
        this.entLeihungsGeb_hr = entLeihungsGeb_hr;
    }
    public int getAnzahlentlehnungen() {
        return AnzahlEntlehnungen;
    }

    public void setAnzahlentlehnungen(int AnzahlEntlehnungen) {
        this.AnzahlEntlehnungen = AnzahlEntlehnungen;
    }
    public String getRegisseur() {
        return Regisseur;
    }

    public void setRegisseur(String Regisseur) {
        this.Regisseur = Regisseur;
    }


}