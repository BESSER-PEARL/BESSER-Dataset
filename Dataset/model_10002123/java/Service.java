





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private int numeroService;
    private String nomService;
    private String descriptionService;





    private Medecin medecin;


    public Service(
        int numeroService,        String nomService,        String descriptionService    ) {
        this.numeroService = numeroService;
        this.nomService = nomService;
        this.descriptionService = descriptionService;
    }


    public int getNumeroservice() {
        return numeroService;
    }

    public void setNumeroservice(int numeroService) {
        this.numeroService = numeroService;
    }
    public String getNomservice() {
        return nomService;
    }

    public void setNomservice(String nomService) {
        this.nomService = nomService;
    }
    public String getDescriptionservice() {
        return descriptionService;
    }

    public void setDescriptionservice(String descriptionService) {
        this.descriptionService = descriptionService;
    }

    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }

}