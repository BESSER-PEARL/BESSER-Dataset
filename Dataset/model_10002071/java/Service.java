





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String nomService;
    private String descriptionService;
    private int numeroService;





    private Medecin medecin;


    public Service(
        String nomService,        String descriptionService,        int numeroService    ) {
        this.nomService = nomService;
        this.descriptionService = descriptionService;
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