





import java.util.List;
import java.util.ArrayList;

public class CentreHospitalier  {

    private int numeroCentre;
    private String descriptionCentre;
    private String nomCentre;





    private List<Service> services;


    public CentreHospitalier(
        int numeroCentre,        String descriptionCentre,        String nomCentre    ) {
        this.numeroCentre = numeroCentre;
        this.descriptionCentre = descriptionCentre;
        this.nomCentre = nomCentre;
        this.services = new ArrayList<>();
    }

    public CentreHospitalier(
        int numeroCentre,        String descriptionCentre,        String nomCentre        ArrayList<Service> services    ) {
        this.numeroCentre = numeroCentre;
        this.descriptionCentre = descriptionCentre;
        this.nomCentre = nomCentre;
        this.services = services;
    }

    public int getNumerocentre() {
        return numeroCentre;
    }

    public void setNumerocentre(int numeroCentre) {
        this.numeroCentre = numeroCentre;
    }
    public String getDescriptioncentre() {
        return descriptionCentre;
    }

    public void setDescriptioncentre(String descriptionCentre) {
        this.descriptionCentre = descriptionCentre;
    }
    public String getNomcentre() {
        return nomCentre;
    }

    public void setNomcentre(String nomCentre) {
        this.nomCentre = nomCentre;
    }

    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}