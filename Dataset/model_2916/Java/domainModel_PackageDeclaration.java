





import java.util.List;
import java.util.ArrayList;

public class domainModel_PackageDeclaration extends AbstractElement {

    private String name;





    private List<domainModel_AbstractElement> domainmodel_abstractelements;


    public domainModel_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.domainmodel_abstractelements = new ArrayList<>();
    }

    public domainModel_PackageDeclaration(
        String name        ArrayList<domainModel_AbstractElement> domainmodel_abstractelements    ) {
        this.name = name;
        this.domainmodel_abstractelements = domainmodel_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<domainModel_AbstractElement> getDomainmodel_abstractelements() {
        return domainmodel_abstractelements;
    }

    public void addDomainmodel_abstractelement(Domainmodel_abstractelement domainmodel_abstractelement) {
        this.domainmodel_abstractelements.add(domainmodel_abstractelement);
    }

}