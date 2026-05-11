





import java.util.List;
import java.util.ArrayList;

public class simpleUML_UMLAttribute  {

    private String umlName;





    private simpleUML_UMLClass simpleuml_umlclass;


    public simpleUML_UMLAttribute(
        String umlName    ) {
        this.umlName = umlName;
    }


    public String getUmlname() {
        return umlName;
    }

    public void setUmlname(String umlName) {
        this.umlName = umlName;
    }

    public simpleUML_UMLClass getSimpleuml_umlclass() {
        return simpleuml_umlclass;
    }

    public void setSimpleuml_umlclass(simpleUML_UMLClass simpleuml_umlclass) {
        this.simpleuml_umlclass = simpleuml_umlclass;
    }

}