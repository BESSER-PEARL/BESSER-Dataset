





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Conducteur  {

    private String datePermi;





    private List<Covoiturage_Trajet> covoiturage_trajets;




    private Covoiturage_Voiture covoiturage_voiture;


    public Covoiturage_Conducteur(
        String datePermi    ) {
        this.datePermi = datePermi;
        this.covoiturage_trajets = new ArrayList<>();
    }

    public Covoiturage_Conducteur(
        String datePermi        ArrayList<Covoiturage_Trajet> covoiturage_trajets    ) {
        this.datePermi = datePermi;
        this.covoiturage_trajets = covoiturage_trajets;
    }

    public String getDatepermi() {
        return datePermi;
    }

    public void setDatepermi(String datePermi) {
        this.datePermi = datePermi;
    }

    public List<Covoiturage_Trajet> getCovoiturage_trajets() {
        return covoiturage_trajets;
    }

    public void addCovoiturage_trajet(Covoiturage_trajet covoiturage_trajet) {
        this.covoiturage_trajets.add(covoiturage_trajet);
    }
    public Covoiturage_Voiture getCovoiturage_voiture() {
        return covoiturage_voiture;
    }

    public void setCovoiturage_voiture(Covoiturage_Voiture covoiturage_voiture) {
        this.covoiturage_voiture = covoiturage_voiture;
    }

}