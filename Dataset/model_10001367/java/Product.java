





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int prijs;
    private String naam;
    private int voorraad;
    private boolean actief;
    private String beschrijving;





    private List<Bestelregel> bestelregels;




    private List<Klant> klants;




    private List<Beheerder> beheerders;


    public Product(
        int prijs,        String naam,        int voorraad,        boolean actief,        String beschrijving    ) {
        this.prijs = prijs;
        this.naam = naam;
        this.voorraad = voorraad;
        this.actief = actief;
        this.beschrijving = beschrijving;
        this.bestelregels = new ArrayList<>();
        this.klants = new ArrayList<>();
        this.beheerders = new ArrayList<>();
    }

    public Product(
        int prijs,        String naam,        int voorraad,        boolean actief,        String beschrijving        ArrayList<Bestelregel> bestelregels,        ArrayList<Klant> klants,        ArrayList<Beheerder> beheerders    ) {
        this.prijs = prijs;
        this.naam = naam;
        this.voorraad = voorraad;
        this.actief = actief;
        this.beschrijving = beschrijving;
        this.bestelregels = bestelregels;
        this.klants = klants;
        this.beheerders = beheerders;
    }

    public int getPrijs() {
        return prijs;
    }

    public void setPrijs(int prijs) {
        this.prijs = prijs;
    }
    public String getNaam() {
        return naam;
    }

    public void setNaam(String naam) {
        this.naam = naam;
    }
    public int getVoorraad() {
        return voorraad;
    }

    public void setVoorraad(int voorraad) {
        this.voorraad = voorraad;
    }
    public boolean getActief() {
        return actief;
    }

    public void setActief(boolean actief) {
        this.actief = actief;
    }
    public String getBeschrijving() {
        return beschrijving;
    }

    public void setBeschrijving(String beschrijving) {
        this.beschrijving = beschrijving;
    }

    public List<Bestelregel> getBestelregels() {
        return bestelregels;
    }

    public void addBestelregel(Bestelregel bestelregel) {
        this.bestelregels.add(bestelregel);
    }
    public List<Klant> getKlants() {
        return klants;
    }

    public void addKlant(Klant klant) {
        this.klants.add(klant);
    }
    public List<Beheerder> getBeheerders() {
        return beheerders;
    }

    public void addBeheerder(Beheerder beheerder) {
        this.beheerders.add(beheerder);
    }

}