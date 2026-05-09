





import java.util.List;
import java.util.ArrayList;

public class org_structure_Enumeration extends DataType {






    private List<structure_EnumerationLiteral> structure_enumerationliterals;


    public org_structure_Enumeration(
    ) {
        super(
        );
        this.structure_enumerationliterals = new ArrayList<>();
    }

    public org_structure_Enumeration(
        ArrayList<structure_EnumerationLiteral> structure_enumerationliterals    ) {
        this.structure_enumerationliterals = structure_enumerationliterals;
    }


    public List<structure_EnumerationLiteral> getStructure_enumerationliterals() {
        return structure_enumerationliterals;
    }

    public void addStructure_enumerationliteral(Structure_enumerationliteral structure_enumerationliteral) {
        this.structure_enumerationliterals.add(structure_enumerationliteral);
    }

}