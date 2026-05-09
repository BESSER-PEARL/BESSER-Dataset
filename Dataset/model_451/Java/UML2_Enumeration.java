





import java.util.List;
import java.util.ArrayList;

public class UML2_Enumeration extends DataType {






    private List<UML2_EnumerationLiteral> uml2_enumerationliterals;




    private UML2_EnumerationLiteral uml2_enumerationliteral;


    public UML2_Enumeration(
    ) {
        super(
        );
        this.uml2_enumerationliterals = new ArrayList<>();
    }

    public UML2_Enumeration(
        ArrayList<UML2_EnumerationLiteral> uml2_enumerationliterals    ) {
        this.uml2_enumerationliterals = uml2_enumerationliterals;
    }


    public List<UML2_EnumerationLiteral> getUml2_enumerationliterals() {
        return uml2_enumerationliterals;
    }

    public void addUml2_enumerationliteral(Uml2_enumerationliteral uml2_enumerationliteral) {
        this.uml2_enumerationliterals.add(uml2_enumerationliteral);
    }
    public UML2_EnumerationLiteral getUml2_enumerationliteral() {
        return uml2_enumerationliteral;
    }

    public void setUml2_enumerationliteral(UML2_EnumerationLiteral uml2_enumerationliteral) {
        this.uml2_enumerationliteral = uml2_enumerationliteral;
    }

}