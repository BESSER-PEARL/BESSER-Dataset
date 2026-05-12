





import java.util.List;
import java.util.ArrayList;

public class Agenda  {

    private String annee;





    private Medecin medecin;




    private AgendaPartage agendapartage;




    private List<RDV> rdvs;


    public Agenda(
        String annee    ) {
        this.annee = annee;
        this.rdvs = new ArrayList<>();
    }

    public Agenda(
        String annee        ArrayList<RDV> rdvs    ) {
        this.annee = annee;
        this.rdvs = rdvs;
    }

    public String getAnnee() {
        return annee;
    }

    public void setAnnee(String annee) {
        this.annee = annee;
    }

    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }
    public AgendaPartage getAgendapartage() {
        return agendapartage;
    }

    public void setAgendapartage(AgendaPartage agendapartage) {
        this.agendapartage = agendapartage;
    }
    public List<RDV> getRdvs() {
        return rdvs;
    }

    public void addRdv(Rdv rdv) {
        this.rdvs.add(rdv);
    }

}