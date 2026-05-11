





import java.util.List;
import java.util.ArrayList;

public class UML_14_Method extends NamedElement {

    private String body;
    private String visibility;





    private UML_14_Class uml_14_class;




    private List<UML_14_Parameter> uml_14_parameters;


    public UML_14_Method(
        String body,        String visibility    ) {
        super(
        );
        this.body = body;
        this.visibility = visibility;
        this.uml_14_parameters = new ArrayList<>();
    }

    public UML_14_Method(
        String body,        String visibility        ArrayList<UML_14_Parameter> uml_14_parameters    ) {
        this.body = body;
        this.visibility = visibility;
        this.uml_14_parameters = uml_14_parameters;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML_14_Class getUml_14_class() {
        return uml_14_class;
    }

    public void setUml_14_class(UML_14_Class uml_14_class) {
        this.uml_14_class = uml_14_class;
    }
    public List<UML_14_Parameter> getUml_14_parameters() {
        return uml_14_parameters;
    }

    public void addUml_14_parameter(Uml_14_parameter uml_14_parameter) {
        this.uml_14_parameters.add(uml_14_parameter);
    }

}