





import java.util.List;
import java.util.ArrayList;

public class myDsl_PackageDeclaration extends AbstractElement {

    private String name;





    private List<myDsl_AbstractElement> mydsl_abstractelements;


    public myDsl_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.mydsl_abstractelements = new ArrayList<>();
    }

    public myDsl_PackageDeclaration(
        String name        ArrayList<myDsl_AbstractElement> mydsl_abstractelements    ) {
        this.name = name;
        this.mydsl_abstractelements = mydsl_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myDsl_AbstractElement> getMydsl_abstractelements() {
        return mydsl_abstractelements;
    }

    public void addMydsl_abstractelement(Mydsl_abstractelement mydsl_abstractelement) {
        this.mydsl_abstractelements.add(mydsl_abstractelement);
    }

}