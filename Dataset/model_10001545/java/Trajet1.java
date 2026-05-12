





import java.util.List;
import java.util.ArrayList;

public class Trajet1  {

    private None lieuFin;
    private String dateFin;
    private None lieudebut;
    private String datedebut;



    public Trajet1(
        None lieuFin,        String dateFin,        None lieudebut,        String datedebut    ) {
        this.lieuFin = lieuFin;
        this.dateFin = dateFin;
        this.lieudebut = lieudebut;
        this.datedebut = datedebut;
    }


    public None getLieufin() {
        return lieuFin;
    }

    public void setLieufin(None lieuFin) {
        this.lieuFin = lieuFin;
    }
    public String getDatefin() {
        return dateFin;
    }

    public void setDatefin(String dateFin) {
        this.dateFin = dateFin;
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