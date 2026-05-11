





import java.util.List;
import java.util.ArrayList;

public class UML_14_Enumeration extends DataType {






    private UML_14_EnumerationLiteral uml_14_enumerationliteral;




    private List<UML_14_EnumerationLiteral> uml_14_enumerationliterals;


    public UML_14_Enumeration(
    ) {
        super(
        );
        this.uml_14_enumerationliterals = new ArrayList<>();
    }

    public UML_14_Enumeration(
        ArrayList<UML_14_EnumerationLiteral> uml_14_enumerationliterals    ) {
        this.uml_14_enumerationliterals = uml_14_enumerationliterals;
    }


    public UML_14_EnumerationLiteral getUml_14_enumerationliteral() {
        return uml_14_enumerationliteral;
    }

    public void setUml_14_enumerationliteral(UML_14_EnumerationLiteral uml_14_enumerationliteral) {
        this.uml_14_enumerationliteral = uml_14_enumerationliteral;
    }
    public List<UML_14_EnumerationLiteral> getUml_14_enumerationliterals() {
        return uml_14_enumerationliterals;
    }

    public void addUml_14_enumerationliteral(Uml_14_enumerationliteral uml_14_enumerationliteral) {
        this.uml_14_enumerationliterals.add(uml_14_enumerationliteral);
    }

}