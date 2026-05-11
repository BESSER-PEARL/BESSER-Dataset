





import java.util.List;
import java.util.ArrayList;

public class domainDsl_PackageDeclaration extends AbstractElement {

    private String name;





    private List<domainDsl_AbstractElement> domaindsl_abstractelements;


    public domainDsl_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.domaindsl_abstractelements = new ArrayList<>();
    }

    public domainDsl_PackageDeclaration(
        String name        ArrayList<domainDsl_AbstractElement> domaindsl_abstractelements    ) {
        this.name = name;
        this.domaindsl_abstractelements = domaindsl_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<domainDsl_AbstractElement> getDomaindsl_abstractelements() {
        return domaindsl_abstractelements;
    }

    public void addDomaindsl_abstractelement(Domaindsl_abstractelement domaindsl_abstractelement) {
        this.domaindsl_abstractelements.add(domaindsl_abstractelement);
    }

}