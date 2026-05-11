





import java.util.List;
import java.util.ArrayList;

public class UML_Enumeration extends Class {






    private List<UML_EnumerationLiteral> uml_enumerationliterals;




    private UML_EnumerationLiteral uml_enumerationliteral;




    private UML_EnumerationLiteral uml_enumerationliteral;


    public UML_Enumeration(
    ) {
        super(
        );
        this.uml_enumerationliterals = new ArrayList<>();
    }

    public UML_Enumeration(
        ArrayList<UML_EnumerationLiteral> uml_enumerationliterals    ) {
        this.uml_enumerationliterals = uml_enumerationliterals;
    }


    public List<UML_EnumerationLiteral> getUml_enumerationliterals() {
        return uml_enumerationliterals;
    }

    public void addUml_enumerationliteral(Uml_enumerationliteral uml_enumerationliteral) {
        this.uml_enumerationliterals.add(uml_enumerationliteral);
    }
    public UML_EnumerationLiteral getUml_enumerationliteral() {
        return uml_enumerationliteral;
    }

    public void setUml_enumerationliteral(UML_EnumerationLiteral uml_enumerationliteral) {
        this.uml_enumerationliteral = uml_enumerationliteral;
    }
    public UML_EnumerationLiteral getUml_enumerationliteral() {
        return uml_enumerationliteral;
    }

    public void setUml_enumerationliteral(UML_EnumerationLiteral uml_enumerationliteral) {
        this.uml_enumerationliteral = uml_enumerationliteral;
    }

}