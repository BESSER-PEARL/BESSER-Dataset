





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String descriptionService;
    private String nomService;
    private int numeroService;





    private Medecin medecin;


    public Service(
        String descriptionService,        String nomService,        int numeroService    ) {
        this.descriptionService = descriptionService;
        this.nomService = nomService;
        this.numeroService = numeroService;
    }


    public String getDescriptionservice() {
        return descriptionService;
    }

    public void setDescriptionservice(String descriptionService) {
        this.descriptionService = descriptionService;
    }
    public String getNomservice() {
        return nomService;
    }

    public void setNomservice(String nomService) {
        this.nomService = nomService;
    }
    public int getNumeroservice() {
        return numeroService;
    }

    public void setNumeroservice(int numeroService) {
        this.numeroService = numeroService;
    }

    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }

}