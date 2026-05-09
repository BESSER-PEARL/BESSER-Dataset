





import java.util.List;
import java.util.ArrayList;

public class uml_Model  {

    private String name;





    private List<uml_PackageableElement> uml_packageableelements;


    public uml_Model(
        String name    ) {
        this.name = name;
        this.uml_packageableelements = new ArrayList<>();
    }

    public uml_Model(
        String name        ArrayList<uml_PackageableElement> uml_packageableelements    ) {
        this.name = name;
        this.uml_packageableelements = uml_packageableelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<uml_PackageableElement> getUml_packageableelements() {
        return uml_packageableelements;
    }

    public void addUml_packageableelement(Uml_packageableelement uml_packageableelement) {
        this.uml_packageableelements.add(uml_packageableelement);
    }

}