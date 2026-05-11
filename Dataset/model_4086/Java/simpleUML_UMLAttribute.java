





import java.util.List;
import java.util.ArrayList;

public class simpleUML_UMLAttribute  {

    private String umlName;





    private simpleUML_SimpleClass simpleuml_simpleclass;


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

    public simpleUML_SimpleClass getSimpleuml_simpleclass() {
        return simpleuml_simpleclass;
    }

    public void setSimpleuml_simpleclass(simpleUML_SimpleClass simpleuml_simpleclass) {
        this.simpleuml_simpleclass = simpleuml_simpleclass;
    }

}