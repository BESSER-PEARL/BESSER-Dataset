





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_DomainElement  {

    private String id;





    private List<DEAssociation> deassociations;


    public spinefm_MSPLModel_DomainElement(
        String id    ) {
        this.id = id;
        this.deassociations = new ArrayList<>();
    }

    public spinefm_MSPLModel_DomainElement(
        String id        ArrayList<DEAssociation> deassociations    ) {
        this.id = id;
        this.deassociations = deassociations;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<DEAssociation> getDeassociations() {
        return deassociations;
    }

    public void addDeassociation(Deassociation deassociation) {
        this.deassociations.add(deassociation);
    }

}