





import java.util.List;
import java.util.ArrayList;

public class domainmodel_PackageDec extends AbstractElement {

    private String name;





    private List<domainmodel_AbstractElement> domainmodel_abstractelements;


    public domainmodel_PackageDec(
        String name    ) {
        super(
        );
        this.name = name;
        this.domainmodel_abstractelements = new ArrayList<>();
    }

    public domainmodel_PackageDec(
        String name        ArrayList<domainmodel_AbstractElement> domainmodel_abstractelements    ) {
        this.name = name;
        this.domainmodel_abstractelements = domainmodel_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<domainmodel_AbstractElement> getDomainmodel_abstractelements() {
        return domainmodel_abstractelements;
    }

    public void addDomainmodel_abstractelement(Domainmodel_abstractelement domainmodel_abstractelement) {
        this.domainmodel_abstractelements.add(domainmodel_abstractelement);
    }

}