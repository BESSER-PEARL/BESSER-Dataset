





import java.util.List;
import java.util.ArrayList;

public class emof_Enumeration extends DataType {






    private List<emof_EnumerationLiteral> emof_enumerationliterals;




    private emof_EnumerationLiteral emof_enumerationliteral;


    public emof_Enumeration(
    ) {
        super(
        );
        this.emof_enumerationliterals = new ArrayList<>();
    }

    public emof_Enumeration(
        ArrayList<emof_EnumerationLiteral> emof_enumerationliterals    ) {
        this.emof_enumerationliterals = emof_enumerationliterals;
    }


    public List<emof_EnumerationLiteral> getEmof_enumerationliterals() {
        return emof_enumerationliterals;
    }

    public void addEmof_enumerationliteral(Emof_enumerationliteral emof_enumerationliteral) {
        this.emof_enumerationliterals.add(emof_enumerationliteral);
    }
    public emof_EnumerationLiteral getEmof_enumerationliteral() {
        return emof_enumerationliteral;
    }

    public void setEmof_enumerationliteral(emof_EnumerationLiteral emof_enumerationliteral) {
        this.emof_enumerationliteral = emof_enumerationliteral;
    }

}