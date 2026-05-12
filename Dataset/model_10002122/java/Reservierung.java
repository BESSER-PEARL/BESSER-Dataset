





import java.util.List;
import java.util.ArrayList;

public class Reservierung  {

    private String reservierungsEnde;
    private String reservierungsDatum;





    private Kunde kunde;




    private List<Exemplar> exemplars;


    public Reservierung(
        String reservierungsEnde,        String reservierungsDatum    ) {
        this.reservierungsEnde = reservierungsEnde;
        this.reservierungsDatum = reservierungsDatum;
        this.exemplars = new ArrayList<>();
    }

    public Reservierung(
        String reservierungsEnde,        String reservierungsDatum        ArrayList<Exemplar> exemplars    ) {
        this.reservierungsEnde = reservierungsEnde;
        this.reservierungsDatum = reservierungsDatum;
        this.exemplars = exemplars;
    }

    public String getReservierungsende() {
        return reservierungsEnde;
    }

    public void setReservierungsende(String reservierungsEnde) {
        this.reservierungsEnde = reservierungsEnde;
    }
    public String getReservierungsdatum() {
        return reservierungsDatum;
    }

    public void setReservierungsdatum(String reservierungsDatum) {
        this.reservierungsDatum = reservierungsDatum;
    }

    public Kunde getKunde() {
        return kunde;
    }

    public void setKunde(Kunde kunde) {
        this.kunde = kunde;
    }
    public List<Exemplar> getExemplars() {
        return exemplars;
    }

    public void addExemplar(Exemplar exemplar) {
        this.exemplars.add(exemplar);
    }

}