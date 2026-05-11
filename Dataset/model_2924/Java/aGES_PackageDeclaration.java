





import java.util.List;
import java.util.ArrayList;

public class aGES_PackageDeclaration extends AbstractElement {

    private String name;





    private List<aGES_AbstractElement> ages_abstractelements;


    public aGES_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.ages_abstractelements = new ArrayList<>();
    }

    public aGES_PackageDeclaration(
        String name        ArrayList<aGES_AbstractElement> ages_abstractelements    ) {
        this.name = name;
        this.ages_abstractelements = ages_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<aGES_AbstractElement> getAges_abstractelements() {
        return ages_abstractelements;
    }

    public void addAges_abstractelement(Ages_abstractelement ages_abstractelement) {
        this.ages_abstractelements.add(ages_abstractelement);
    }

}