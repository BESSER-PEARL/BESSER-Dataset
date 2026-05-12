




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Recherche_Avanc_e  {

    private int NbParticipants;
    private None Association;
    private LocalDate Date;
    private String Titre;
    private String Pays;



    public Recherche_Avanc_e(
        int NbParticipants,        None Association,        LocalDate Date,        String Titre,        String Pays    ) {
        this.NbParticipants = NbParticipants;
        this.Association = Association;
        this.Date = Date;
        this.Titre = Titre;
        this.Pays = Pays;
    }


    public int getNbparticipants() {
        return NbParticipants;
    }

    public void setNbparticipants(int NbParticipants) {
        this.NbParticipants = NbParticipants;
    }
    public None getAssociation() {
        return Association;
    }

    public void setAssociation(None Association) {
        this.Association = Association;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public String getTitre() {
        return Titre;
    }

    public void setTitre(String Titre) {
        this.Titre = Titre;
    }
    public String getPays() {
        return Pays;
    }

    public void setPays(String Pays) {
        this.Pays = Pays;
    }


}