





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_MultipleSoftwareProductLine  {






    private List<DEAssociation> deassociations;




    private List<DomainElement> domainelements;


    public spinefm_MSPLModel_MultipleSoftwareProductLine(
    ) {
        this.deassociations = new ArrayList<>();
        this.domainelements = new ArrayList<>();
    }

    public spinefm_MSPLModel_MultipleSoftwareProductLine(
        ArrayList<DEAssociation> deassociations,        ArrayList<DomainElement> domainelements    ) {
        this.deassociations = deassociations;
        this.domainelements = domainelements;
    }


    public List<DEAssociation> getDeassociations() {
        return deassociations;
    }

    public void addDeassociation(Deassociation deassociation) {
        this.deassociations.add(deassociation);
    }
    public List<DomainElement> getDomainelements() {
        return domainelements;
    }

    public void addDomainelement(Domainelement domainelement) {
        this.domainelements.add(domainelement);
    }

}