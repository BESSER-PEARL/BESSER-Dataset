





import java.util.List;
import java.util.ArrayList;

public class Trajet2  {

    private int placesRestantes;
    private String description;
    private String dateFin;
    private None lieuFin;
    private int prix;
    private String datedebut;
    private None lieudebut;



    public Trajet2(
        int placesRestantes,        String description,        String dateFin,        None lieuFin,        int prix,        String datedebut,        None lieudebut    ) {
        this.placesRestantes = placesRestantes;
        this.description = description;
        this.dateFin = dateFin;
        this.lieuFin = lieuFin;
        this.prix = prix;
        this.datedebut = datedebut;
        this.lieudebut = lieudebut;
    }


    public int getPlacesrestantes() {
        return placesRestantes;
    }

    public void setPlacesrestantes(int placesRestantes) {
        this.placesRestantes = placesRestantes;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDatefin() {
        return dateFin;
    }

    public void setDatefin(String dateFin) {
        this.dateFin = dateFin;
    }
    public None getLieufin() {
        return lieuFin;
    }

    public void setLieufin(None lieuFin) {
        this.lieuFin = lieuFin;
    }
    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public String getDatedebut() {
        return datedebut;
    }

    public void setDatedebut(String datedebut) {
        this.datedebut = datedebut;
    }
    public None getLieudebut() {
        return lieudebut;
    }

    public void setLieudebut(None lieudebut) {
        this.lieudebut = lieudebut;
    }


}