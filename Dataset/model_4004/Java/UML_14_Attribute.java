





import java.util.List;
import java.util.ArrayList;

public class UML_14_Attribute extends NamedElement {

    private String visibility;
    private String initialValue;





    private UML_14_DataType uml_14_datatype;




    private UML_14_MultiplicityRange uml_14_multiplicityrange;


    public UML_14_Attribute(
        String visibility,        String initialValue    ) {
        super(
        );
        this.visibility = visibility;
        this.initialValue = initialValue;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }

    public UML_14_DataType getUml_14_datatype() {
        return uml_14_datatype;
    }

    public void setUml_14_datatype(UML_14_DataType uml_14_datatype) {
        this.uml_14_datatype = uml_14_datatype;
    }
    public UML_14_MultiplicityRange getUml_14_multiplicityrange() {
        return uml_14_multiplicityrange;
    }

    public void setUml_14_multiplicityrange(UML_14_MultiplicityRange uml_14_multiplicityrange) {
        this.uml_14_multiplicityrange = uml_14_multiplicityrange;
    }

}