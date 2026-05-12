





import java.util.List;
import java.util.ArrayList;

public class Klant  {

    private String telefoonnummer;
    private String geboortedatum;



    public Klant(
        String telefoonnummer,        String geboortedatum    ) {
        this.telefoonnummer = telefoonnummer;
        this.geboortedatum = geboortedatum;
    }


    public String getTelefoonnummer() {
        return telefoonnummer;
    }

    public void setTelefoonnummer(String telefoonnummer) {
        this.telefoonnummer = telefoonnummer;
    }
    public String getGeboortedatum() {
        return geboortedatum;
    }

    public void setGeboortedatum(String geboortedatum) {
        this.geboortedatum = geboortedatum;
    }


}