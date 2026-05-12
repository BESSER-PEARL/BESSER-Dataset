




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Session  {

    private LocalDate date_fin;
    private String adresse;
    private LocalDate date_debut;
    private int id_session;
    private String label;





    private List<Formateur> formateurs;




    private List<Etudiant> etudiants;


    public Session(
        LocalDate date_fin,        String adresse,        LocalDate date_debut,        int id_session,        String label    ) {
        this.date_fin = date_fin;
        this.adresse = adresse;
        this.date_debut = date_debut;
        this.id_session = id_session;
        this.label = label;
        this.formateurs = new ArrayList<>();
        this.etudiants = new ArrayList<>();
    }

    public Session(
        LocalDate date_fin,        String adresse,        LocalDate date_debut,        int id_session,        String label        ArrayList<Formateur> formateurs,        ArrayList<Etudiant> etudiants    ) {
        this.date_fin = date_fin;
        this.adresse = adresse;
        this.date_debut = date_debut;
        this.id_session = id_session;
        this.label = label;
        this.formateurs = formateurs;
        this.etudiants = etudiants;
    }

    public LocalDate getDate_fin() {
        return date_fin;
    }

    public void setDate_fin(LocalDate date_fin) {
        this.date_fin = date_fin;
    }
    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public LocalDate getDate_debut() {
        return date_debut;
    }

    public void setDate_debut(LocalDate date_debut) {
        this.date_debut = date_debut;
    }
    public int getId_session() {
        return id_session;
    }

    public void setId_session(int id_session) {
        this.id_session = id_session;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<Formateur> getFormateurs() {
        return formateurs;
    }

    public void addFormateur(Formateur formateur) {
        this.formateurs.add(formateur);
    }
    public List<Etudiant> getEtudiants() {
        return etudiants;
    }

    public void addEtudiant(Etudiant etudiant) {
        this.etudiants.add(etudiant);
    }

}