





import java.util.List;
import java.util.ArrayList;

public class Trajet1  {

    private String dateFin;
    private None lieuFin;
    private None lieudebut;
    private String datedebut;



    public Trajet1(
        String dateFin,        None lieuFin,        None lieudebut,        String datedebut    ) {
        this.dateFin = dateFin;
        this.lieuFin = lieuFin;
        this.lieudebut = lieudebut;
        this.datedebut = datedebut;
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
    public None getLieudebut() {
        return lieudebut;
    }

    public void setLieudebut(None lieudebut) {
        this.lieudebut = lieudebut;
    }
    public String getDatedebut() {
        return datedebut;
    }

    public void setDatedebut(String datedebut) {
        this.datedebut = datedebut;
    }


}