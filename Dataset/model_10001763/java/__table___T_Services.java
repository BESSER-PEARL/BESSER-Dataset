




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class __table___T_Services  {

    private String description;
    private int nbParticipants;
    private String titre;
    private int numeroUtilisateur;
    private String type;
    private LocalDate date;
    private int numeroService;



    public __table___T_Services(
        String description,        int nbParticipants,        String titre,        int numeroUtilisateur,        String type,        LocalDate date,        int numeroService    ) {
        this.description = description;
        this.nbParticipants = nbParticipants;
        this.titre = titre;
        this.numeroUtilisateur = numeroUtilisateur;
        this.type = type;
        this.date = date;
        this.numeroService = numeroService;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNbparticipants() {
        return nbParticipants;
    }

    public void setNbparticipants(int nbParticipants) {
        this.nbParticipants = nbParticipants;
    }
    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }
    public int getNumeroutilisateur() {
        return numeroUtilisateur;
    }

    public void setNumeroutilisateur(int numeroUtilisateur) {
        this.numeroUtilisateur = numeroUtilisateur;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getNumeroservice() {
        return numeroService;
    }

    public void setNumeroservice(int numeroService) {
        this.numeroService = numeroService;
    }


}