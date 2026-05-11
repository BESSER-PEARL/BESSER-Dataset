





import java.util.List;
import java.util.ArrayList;

public class myTuto_PackageDeclaration extends AbstractElement {

    private String name;





    private List<myTuto_AbstractElement> mytuto_abstractelements;


    public myTuto_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.mytuto_abstractelements = new ArrayList<>();
    }

    public myTuto_PackageDeclaration(
        String name        ArrayList<myTuto_AbstractElement> mytuto_abstractelements    ) {
        this.name = name;
        this.mytuto_abstractelements = mytuto_abstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myTuto_AbstractElement> getMytuto_abstractelements() {
        return mytuto_abstractelements;
    }

    public void addMytuto_abstractelement(Mytuto_abstractelement mytuto_abstractelement) {
        this.mytuto_abstractelements.add(mytuto_abstractelement);
    }

}