





import java.util.List;
import java.util.ArrayList;

public class UML_14_Parameter extends NamedElement {

    private String kind;
    private String defaultValue;





    private UML_14_Primitive uml_14_primitive;




    private UML_14_Method uml_14_method;


    public UML_14_Parameter(
        String kind,        String defaultValue    ) {
        super(
        );
        this.kind = kind;
        this.defaultValue = defaultValue;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public UML_14_Primitive getUml_14_primitive() {
        return uml_14_primitive;
    }

    public void setUml_14_primitive(UML_14_Primitive uml_14_primitive) {
        this.uml_14_primitive = uml_14_primitive;
    }
    public UML_14_Method getUml_14_method() {
        return uml_14_method;
    }

    public void setUml_14_method(UML_14_Method uml_14_method) {
        this.uml_14_method = uml_14_method;
    }

}