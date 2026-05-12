





import java.util.List;
import java.util.ArrayList;

public class Prestation  {

    private int id_client;
    private String date_debut;
    private boolean lieu;
    private String horaires;
    private int nb_stagiaires;
    private int id_formation;
    private String duree;
    private int id_formateur;
    private String date_fin;
    private int id_type;





    private Type type;




    private Formation formation;




    private DevisEntete devisentete;




    private Client client;


    public Prestation(
        int id_client,        String date_debut,        boolean lieu,        String horaires,        int nb_stagiaires,        int id_formation,        String duree,        int id_formateur,        String date_fin,        int id_type    ) {
        this.id_client = id_client;
        this.date_debut = date_debut;
        this.lieu = lieu;
        this.horaires = horaires;
        this.nb_stagiaires = nb_stagiaires;
        this.id_formation = id_formation;
        this.duree = duree;
        this.id_formateur = id_formateur;
        this.date_fin = date_fin;
        this.id_type = id_type;
    }


    public int getId_client() {
        return id_client;
    }

    public void setId_client(int id_client) {
        this.id_client = id_client;
    }
    public String getDate_debut() {
        return date_debut;
    }

    public void setDate_debut(String date_debut) {
        this.date_debut = date_debut;
    }
    public boolean getLieu() {
        return lieu;
    }

    public void setLieu(boolean lieu) {
        this.lieu = lieu;
    }
    public String getHoraires() {
        return horaires;
    }

    public void setHoraires(String horaires) {
        this.horaires = horaires;
    }
    public int getNb_stagiaires() {
        return nb_stagiaires;
    }

    public void setNb_stagiaires(int nb_stagiaires) {
        this.nb_stagiaires = nb_stagiaires;
    }
    public int getId_formation() {
        return id_formation;
    }

    public void setId_formation(int id_formation) {
        this.id_formation = id_formation;
    }
    public String getDuree() {
        return duree;
    }

    public void setDuree(String duree) {
        this.duree = duree;
    }
    public int getId_formateur() {
        return id_formateur;
    }

    public void setId_formateur(int id_formateur) {
        this.id_formateur = id_formateur;
    }
    public String getDate_fin() {
        return date_fin;
    }

    public void setDate_fin(String date_fin) {
        this.date_fin = date_fin;
    }
    public int getId_type() {
        return id_type;
    }

    public void setId_type(int id_type) {
        this.id_type = id_type;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public Formation getFormation() {
        return formation;
    }

    public void setFormation(Formation formation) {
        this.formation = formation;
    }
    public DevisEntete getDevisentete() {
        return devisentete;
    }

    public void setDevisentete(DevisEntete devisentete) {
        this.devisentete = devisentete;
    }
    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}