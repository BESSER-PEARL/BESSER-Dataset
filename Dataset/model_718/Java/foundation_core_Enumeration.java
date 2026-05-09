





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Enumeration extends DataType {






    private List<EnumerationLiteral> enumerationliterals;


    public foundation_core_Enumeration(
    ) {
        super(
        );
        this.enumerationliterals = new ArrayList<>();
    }

    public foundation_core_Enumeration(
        ArrayList<EnumerationLiteral> enumerationliterals    ) {
        this.enumerationliterals = enumerationliterals;
    }


    public List<EnumerationLiteral> getEnumerationliterals() {
        return enumerationliterals;
    }

    public void addEnumerationliteral(Enumerationliteral enumerationliteral) {
        this.enumerationliterals.add(enumerationliteral);
    }

}