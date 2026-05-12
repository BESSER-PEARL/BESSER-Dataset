





import java.util.List;
import java.util.ArrayList;

public class Trajet1  {

    private None lieuFin;
    private String datedebut;
    private None lieudebut;
    private String dateFin;



    public Trajet1(
        None lieuFin,        String datedebut,        None lieudebut,        String dateFin    ) {
        this.lieuFin = lieuFin;
        this.datedebut = datedebut;
        this.lieudebut = lieudebut;
        this.dateFin = dateFin;
    }


    public None getLieufin() {
        return lieuFin;
    }

    public void setLieufin(None lieuFin) {
        this.lieuFin = lieuFin;
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
    public String getDatefin() {
        return dateFin;
    }

    public void setDatefin(String dateFin) {
        this.dateFin = dateFin;
    }


}