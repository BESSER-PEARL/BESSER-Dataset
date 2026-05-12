





import java.util.List;
import java.util.ArrayList;

public class Contactformulier  {

    private String tekst;





    private List<Beheerder> beheerders;




    private Klant klant;


    public Contactformulier(
        String tekst    ) {
        this.tekst = tekst;
        this.beheerders = new ArrayList<>();
    }

    public Contactformulier(
        String tekst        ArrayList<Beheerder> beheerders    ) {
        this.tekst = tekst;
        this.beheerders = beheerders;
    }

    public String getTekst() {
        return tekst;
    }

    public void setTekst(String tekst) {
        this.tekst = tekst;
    }

    public List<Beheerder> getBeheerders() {
        return beheerders;
    }

    public void addBeheerder(Beheerder beheerder) {
        this.beheerders.add(beheerder);
    }
    public Klant getKlant() {
        return klant;
    }

    public void setKlant(Klant klant) {
        this.klant = klant;
    }

}