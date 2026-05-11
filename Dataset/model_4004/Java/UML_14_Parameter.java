





import java.util.List;
import java.util.ArrayList;

public class UML_14_Parameter extends NamedElement {

    private String defaultValue;
    private String kind;





    private UML_14_DataType uml_14_datatype;




    private UML_14_Method uml_14_method;


    public UML_14_Parameter(
        String defaultValue,        String kind    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.kind = kind;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public UML_14_DataType getUml_14_datatype() {
        return uml_14_datatype;
    }

    public void setUml_14_datatype(UML_14_DataType uml_14_datatype) {
        this.uml_14_datatype = uml_14_datatype;
    }
    public UML_14_Method getUml_14_method() {
        return uml_14_method;
    }

    public void setUml_14_method(UML_14_Method uml_14_method) {
        this.uml_14_method = uml_14_method;
    }

}