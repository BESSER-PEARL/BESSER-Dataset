





import java.util.List;
import java.util.ArrayList;

public class Afbeelding  {

    private String naam;
    private String locatie;
    private String datum;





    private List<Nieuwsbericht> nieuwsberichts;




    private List<Product> products;


    public Afbeelding(
        String naam,        String locatie,        String datum    ) {
        this.naam = naam;
        this.locatie = locatie;
        this.datum = datum;
        this.nieuwsberichts = new ArrayList<>();
        this.products = new ArrayList<>();
    }

    public Afbeelding(
        String naam,        String locatie,        String datum        ArrayList<Nieuwsbericht> nieuwsberichts,        ArrayList<Product> products    ) {
        this.naam = naam;
        this.locatie = locatie;
        this.datum = datum;
        this.nieuwsberichts = nieuwsberichts;
        this.products = products;
    }

    public String getNaam() {
        return naam;
    }

    public void setNaam(String naam) {
        this.naam = naam;
    }
    public String getLocatie() {
        return locatie;
    }

    public void setLocatie(String locatie) {
        this.locatie = locatie;
    }
    public String getDatum() {
        return datum;
    }

    public void setDatum(String datum) {
        this.datum = datum;
    }

    public List<Nieuwsbericht> getNieuwsberichts() {
        return nieuwsberichts;
    }

    public void addNieuwsbericht(Nieuwsbericht nieuwsbericht) {
        this.nieuwsberichts.add(nieuwsbericht);
    }
    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}