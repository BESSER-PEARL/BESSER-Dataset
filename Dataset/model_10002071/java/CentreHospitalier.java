





import java.util.List;
import java.util.ArrayList;

public class CentreHospitalier  {

    private int numeroCentre;
    private String nomCentre;
    private String descriptionCentre;





    private List<Service> services;


    public CentreHospitalier(
        int numeroCentre,        String nomCentre,        String descriptionCentre    ) {
        this.numeroCentre = numeroCentre;
        this.nomCentre = nomCentre;
        this.descriptionCentre = descriptionCentre;
        this.services = new ArrayList<>();
    }

    public CentreHospitalier(
        int numeroCentre,        String nomCentre,        String descriptionCentre        ArrayList<Service> services    ) {
        this.numeroCentre = numeroCentre;
        this.nomCentre = nomCentre;
        this.descriptionCentre = descriptionCentre;
        this.services = services;
    }

    public int getNumerocentre() {
        return numeroCentre;
    }

    public void setNumerocentre(int numeroCentre) {
        this.numeroCentre = numeroCentre;
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

    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}