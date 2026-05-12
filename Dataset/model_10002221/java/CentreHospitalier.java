





import java.util.List;
import java.util.ArrayList;

public class CentreHospitalier  {

    private String nomCentre;
    private int numeroCentre;
    private String descriptionCentre;





    private List<Service> services;


    public CentreHospitalier(
        String nomCentre,        int numeroCentre,        String descriptionCentre    ) {
        this.nomCentre = nomCentre;
        this.numeroCentre = numeroCentre;
        this.descriptionCentre = descriptionCentre;
        this.services = new ArrayList<>();
    }

    public CentreHospitalier(
        String nomCentre,        int numeroCentre,        String descriptionCentre        ArrayList<Service> services    ) {
        this.nomCentre = nomCentre;
        this.numeroCentre = numeroCentre;
        this.descriptionCentre = descriptionCentre;
        this.services = services;
    }

    public String getNomcentre() {
        return nomCentre;
    }

    public void setNomcentre(String nomCentre) {
        this.nomCentre = nomCentre;
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

    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}