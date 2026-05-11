





import java.util.List;
import java.util.ArrayList;

public class ling_PackageDeclaration extends AbstractElement {

    private String name;





    private List<ling_AbstractElement> ling_abstractelements;


    public ling_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.ling_abstractelements = new ArrayList<>();
    }

    public ling_PackageDeclaration(
        String name        ArrayList<ling_AbstractElement> ling_abstractelements    ) {
        this.name = name;
        this.ling_abstractelements = ling_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ling_AbstractElement> getLing_abstractelements() {
        return ling_abstractelements;
    }

    public void addLing_abstractelement(Ling_abstractelement ling_abstractelement) {
        this.ling_abstractelements.add(ling_abstractelement);
    }

}