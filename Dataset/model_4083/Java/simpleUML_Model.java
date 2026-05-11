





import java.util.List;
import java.util.ArrayList;

public class simpleUML_Model  {






    private List<simpleUML_UMLClass> simpleuml_umlclasss;


    public simpleUML_Model(
    ) {
        this.simpleuml_umlclasss = new ArrayList<>();
    }

    public simpleUML_Model(
        ArrayList<simpleUML_UMLClass> simpleuml_umlclasss    ) {
        this.simpleuml_umlclasss = simpleuml_umlclasss;
    }


    public List<simpleUML_UMLClass> getSimpleuml_umlclasss() {
        return simpleuml_umlclasss;
    }

    public void addSimpleuml_umlclass(Simpleuml_umlclass simpleuml_umlclass) {
        this.simpleuml_umlclasss.add(simpleuml_umlclass);
    }

}