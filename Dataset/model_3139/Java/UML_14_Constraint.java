





import java.util.List;
import java.util.ArrayList;

public class UML_14_Constraint extends ModelElement {

    private String body;





    private List<UML_14_ModelElement> uml_14_modelelements;




    private UML_14_ModelElement uml_14_modelelement;


    public UML_14_Constraint(
        String body    ) {
        super(
        );
        this.body = body;
        this.uml_14_modelelements = new ArrayList<>();
    }

    public UML_14_Constraint(
        String body        ArrayList<UML_14_ModelElement> uml_14_modelelements    ) {
        this.body = body;
        this.uml_14_modelelements = uml_14_modelelements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<UML_14_ModelElement> getUml_14_modelelements() {
        return uml_14_modelelements;
    }

    public void addUml_14_modelelement(Uml_14_modelelement uml_14_modelelement) {
        this.uml_14_modelelements.add(uml_14_modelelement);
    }
    public UML_14_ModelElement getUml_14_modelelement() {
        return uml_14_modelelement;
    }

    public void setUml_14_modelelement(UML_14_ModelElement uml_14_modelelement) {
        this.uml_14_modelelement = uml_14_modelelement;
    }

}