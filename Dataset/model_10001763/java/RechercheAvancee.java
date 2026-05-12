




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class RechercheAvancee  {

    private int NbParticipants;
    private LocalDate Date;
    private None Association;
    private String Titre;
    private None GenreService;



    public RechercheAvancee(
        int NbParticipants,        LocalDate Date,        None Association,        String Titre,        None GenreService    ) {
        this.NbParticipants = NbParticipants;
        this.Date = Date;
        this.Association = Association;
        this.Titre = Titre;
        this.GenreService = GenreService;
    }


    public int getNbparticipants() {
        return NbParticipants;
    }

    public void setNbparticipants(int NbParticipants) {
        this.NbParticipants = NbParticipants;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public None getAssociation() {
        return Association;
    }

    public void setAssociation(None Association) {
        this.Association = Association;
    }
    public String getTitre() {
        return Titre;
    }

    public void setTitre(String Titre) {
        this.Titre = Titre;
    }
    public None getGenreservice() {
        return GenreService;
    }

    public void setGenreservice(None GenreService) {
        this.GenreService = GenreService;
    }


}