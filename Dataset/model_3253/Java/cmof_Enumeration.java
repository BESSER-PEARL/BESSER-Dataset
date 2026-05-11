





import java.util.List;
import java.util.ArrayList;

public class cmof_Enumeration extends DataType {






    private List<cmof_EnumerationLiteral> cmof_enumerationliterals;




    private cmof_EnumerationLiteral cmof_enumerationliteral;


    public cmof_Enumeration(
    ) {
        super(
        );
        this.cmof_enumerationliterals = new ArrayList<>();
    }

    public cmof_Enumeration(
        ArrayList<cmof_EnumerationLiteral> cmof_enumerationliterals    ) {
        this.cmof_enumerationliterals = cmof_enumerationliterals;
    }


    public List<cmof_EnumerationLiteral> getCmof_enumerationliterals() {
        return cmof_enumerationliterals;
    }

    public void addCmof_enumerationliteral(Cmof_enumerationliteral cmof_enumerationliteral) {
        this.cmof_enumerationliterals.add(cmof_enumerationliteral);
    }
    public cmof_EnumerationLiteral getCmof_enumerationliteral() {
        return cmof_enumerationliteral;
    }

    public void setCmof_enumerationliteral(cmof_EnumerationLiteral cmof_enumerationliteral) {
        this.cmof_enumerationliteral = cmof_enumerationliteral;
    }

}