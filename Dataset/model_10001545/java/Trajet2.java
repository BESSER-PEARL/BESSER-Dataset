





import java.util.List;
import java.util.ArrayList;

public class Trajet2  {

    private int prix;
    private None lieudebut;
    private String dateFin;
    private String datedebut;
    private String description;
    private int placesRestantes;
    private None lieuFin;



    public Trajet2(
        int prix,        None lieudebut,        String dateFin,        String datedebut,        String description,        int placesRestantes,        None lieuFin    ) {
        this.prix = prix;
        this.lieudebut = lieudebut;
        this.dateFin = dateFin;
        this.datedebut = datedebut;
        this.description = description;
        this.placesRestantes = placesRestantes;
        this.lieuFin = lieuFin;
    }


    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public None getLieudebut() {
        return lieudebut;
    }

    public void setLieudebut(None lieudebut) {
        this.lieudebut = lieudebut;
    }
    public String getDatefin() {
        return dateFin;
    }

    public void setDatefin(String dateFin) {
        this.dateFin = dateFin;
    }
    public String getDatedebut() {
        return datedebut;
    }

    public void setDatedebut(String datedebut) {
        this.datedebut = datedebut;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getPlacesrestantes() {
        return placesRestantes;
    }

    public void setPlacesrestantes(int placesRestantes) {
        this.placesRestantes = placesRestantes;
    }
    public None getLieufin() {
        return lieuFin;
    }

    public void setLieufin(None lieuFin) {
        this.lieuFin = lieuFin;
    }


}