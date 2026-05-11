





import java.util.List;
import java.util.ArrayList;

public class simpleUML_UMLClass  {

    private String umlName;





    private List<simpleUML_UMLClass> simpleuml_umlclasss;


    public simpleUML_UMLClass(
        String umlName    ) {
        this.umlName = umlName;
        this.simpleuml_umlclasss = new ArrayList<>();
    }

    public simpleUML_UMLClass(
        String umlName        ArrayList<simpleUML_UMLClass> simpleuml_umlclasss    ) {
        this.umlName = umlName;
        this.simpleuml_umlclasss = simpleuml_umlclasss;
    }

    public String getUmlname() {
        return umlName;
    }

    public void setUmlname(String umlName) {
        this.umlName = umlName;
    }

    public List<simpleUML_UMLClass> getSimpleuml_umlclasss() {
        return simpleuml_umlclasss;
    }

    public void addSimpleuml_umlclass(Simpleuml_umlclass simpleuml_umlclass) {
        this.simpleuml_umlclasss.add(simpleuml_umlclass);
    }

}