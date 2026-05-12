





import java.util.List;
import java.util.ArrayList;

public class CentreHospitalier  {

    private String nomCentre;
    private String descriptionCentre;
    private int numeroCentre;





    private List<Service> services;


    public CentreHospitalier(
        String nomCentre,        String descriptionCentre,        int numeroCentre    ) {
        this.nomCentre = nomCentre;
        this.descriptionCentre = descriptionCentre;
        this.numeroCentre = numeroCentre;
        this.services = new ArrayList<>();
    }

    public CentreHospitalier(
        String nomCentre,        String descriptionCentre,        int numeroCentre        ArrayList<Service> services    ) {
        this.nomCentre = nomCentre;
        this.descriptionCentre = descriptionCentre;
        this.numeroCentre = numeroCentre;
        this.services = services;
    }

    public String getNomcentre() {
        return nomCentre;
    }

    public void setNomcentre(String nomCentre) {
        this.nomCentre = nomCentre;
    }
    public String getDescriptioncentre() {
        return descriptionCentre;
    }

    public void setDescriptioncentre(String descriptionCentre) {
        this.descriptionCentre = descriptionCentre;
    }
    public int getNumerocentre() {
        return numeroCentre;
    }

    public void setNumerocentre(int numeroCentre) {
        this.numeroCentre = numeroCentre;
    }

    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}