





import java.util.List;
import java.util.ArrayList;

public class Employe  {

    private String dateFin;
    private String dateDebut;
    private int joursVacance;
    private int salaire;



    public Employe(
        String dateFin,        String dateDebut,        int joursVacance,        int salaire    ) {
        this.dateFin = dateFin;
        this.dateDebut = dateDebut;
        this.joursVacance = joursVacance;
        this.salaire = salaire;
    }


    public String getDatefin() {
        return dateFin;
    }

    public void setDatefin(String dateFin) {
        this.dateFin = dateFin;
    }
    public String getDatedebut() {
        return dateDebut;
    }

    public void setDatedebut(String dateDebut) {
        this.dateDebut = dateDebut;
    }
    public int getJoursvacance() {
        return joursVacance;
    }

    public void setJoursvacance(int joursVacance) {
        this.joursVacance = joursVacance;
    }
    public int getSalaire() {
        return salaire;
    }

    public void setSalaire(int salaire) {
        this.salaire = salaire;
    }


}