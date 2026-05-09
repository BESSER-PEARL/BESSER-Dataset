





import java.util.List;
import java.util.ArrayList;

public class pivot_Enumeration extends DataType {






    private pivot_EnumerationLiteral pivot_enumerationliteral;




    private List<pivot_EnumerationLiteral> pivot_enumerationliterals;


    public pivot_Enumeration(
    ) {
        super(
        );
        this.pivot_enumerationliterals = new ArrayList<>();
    }

    public pivot_Enumeration(
        ArrayList<pivot_EnumerationLiteral> pivot_enumerationliterals    ) {
        this.pivot_enumerationliterals = pivot_enumerationliterals;
    }


    public pivot_EnumerationLiteral getPivot_enumerationliteral() {
        return pivot_enumerationliteral;
    }

    public void setPivot_enumerationliteral(pivot_EnumerationLiteral pivot_enumerationliteral) {
        this.pivot_enumerationliteral = pivot_enumerationliteral;
    }
    public List<pivot_EnumerationLiteral> getPivot_enumerationliterals() {
        return pivot_enumerationliterals;
    }

    public void addPivot_enumerationliteral(Pivot_enumerationliteral pivot_enumerationliteral) {
        this.pivot_enumerationliterals.add(pivot_enumerationliteral);
    }

}