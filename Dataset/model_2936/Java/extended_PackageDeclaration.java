





import java.util.List;
import java.util.ArrayList;

public class extended_PackageDeclaration extends AbstractElement {

    private String name;





    private List<extended_AbstractElement> extended_abstractelements;


    public extended_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.extended_abstractelements = new ArrayList<>();
    }

    public extended_PackageDeclaration(
        String name        ArrayList<extended_AbstractElement> extended_abstractelements    ) {
        this.name = name;
        this.extended_abstractelements = extended_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<extended_AbstractElement> getExtended_abstractelements() {
        return extended_abstractelements;
    }

    public void addExtended_abstractelement(Extended_abstractelement extended_abstractelement) {
        this.extended_abstractelements.add(extended_abstractelement);
    }

}