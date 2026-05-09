





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Enumeration extends DataType {






    private List<UML2WithID_EnumerationLiteral> uml2withid_enumerationliterals;




    private UML2WithID_EnumerationLiteral uml2withid_enumerationliteral;


    public UML2WithID_Enumeration(
    ) {
        super(
        );
        this.uml2withid_enumerationliterals = new ArrayList<>();
    }

    public UML2WithID_Enumeration(
        ArrayList<UML2WithID_EnumerationLiteral> uml2withid_enumerationliterals    ) {
        this.uml2withid_enumerationliterals = uml2withid_enumerationliterals;
    }


    public List<UML2WithID_EnumerationLiteral> getUml2withid_enumerationliterals() {
        return uml2withid_enumerationliterals;
    }

    public void addUml2withid_enumerationliteral(Uml2withid_enumerationliteral uml2withid_enumerationliteral) {
        this.uml2withid_enumerationliterals.add(uml2withid_enumerationliteral);
    }
    public UML2WithID_EnumerationLiteral getUml2withid_enumerationliteral() {
        return uml2withid_enumerationliteral;
    }

    public void setUml2withid_enumerationliteral(UML2WithID_EnumerationLiteral uml2withid_enumerationliteral) {
        this.uml2withid_enumerationliteral = uml2withid_enumerationliteral;
    }

}