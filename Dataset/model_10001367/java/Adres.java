





import java.util.List;
import java.util.ArrayList;

public class Adres  {

    private String postcode;
    private int huisnummer;
    private String bijvoegsel;
    private String stad;
    private String straatnaam;





    private List<Klant> klants;


    public Adres(
        String postcode,        int huisnummer,        String bijvoegsel,        String stad,        String straatnaam    ) {
        this.postcode = postcode;
        this.huisnummer = huisnummer;
        this.bijvoegsel = bijvoegsel;
        this.stad = stad;
        this.straatnaam = straatnaam;
        this.klants = new ArrayList<>();
    }

    public Adres(
        String postcode,        int huisnummer,        String bijvoegsel,        String stad,        String straatnaam        ArrayList<Klant> klants    ) {
        this.postcode = postcode;
        this.huisnummer = huisnummer;
        this.bijvoegsel = bijvoegsel;
        this.stad = stad;
        this.straatnaam = straatnaam;
        this.klants = klants;
    }

    public String getPostcode() {
        return postcode;
    }

    public void setPostcode(String postcode) {
        this.postcode = postcode;
    }
    public int getHuisnummer() {
        return huisnummer;
    }

    public void setHuisnummer(int huisnummer) {
        this.huisnummer = huisnummer;
    }
    public String getBijvoegsel() {
        return bijvoegsel;
    }

    public void setBijvoegsel(String bijvoegsel) {
        this.bijvoegsel = bijvoegsel;
    }
    public String getStad() {
        return stad;
    }

    public void setStad(String stad) {
        this.stad = stad;
    }
    public String getStraatnaam() {
        return straatnaam;
    }

    public void setStraatnaam(String straatnaam) {
        this.straatnaam = straatnaam;
    }

    public List<Klant> getKlants() {
        return klants;
    }

    public void addKlant(Klant klant) {
        this.klants.add(klant);
    }

}