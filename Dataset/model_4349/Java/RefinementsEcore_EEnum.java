





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EEnum extends EDataType {






    private RefinementsEcore_EEnumLiteral refinementsecore_eenumliteral;




    private List<RefinementsEcore_EEnumLiteral> refinementsecore_eenumliterals;


    public RefinementsEcore_EEnum(
    ) {
        super(
        );
        this.refinementsecore_eenumliterals = new ArrayList<>();
    }

    public RefinementsEcore_EEnum(
        ArrayList<RefinementsEcore_EEnumLiteral> refinementsecore_eenumliterals    ) {
        this.refinementsecore_eenumliterals = refinementsecore_eenumliterals;
    }


    public RefinementsEcore_EEnumLiteral getRefinementsecore_eenumliteral() {
        return refinementsecore_eenumliteral;
    }

    public void setRefinementsecore_eenumliteral(RefinementsEcore_EEnumLiteral refinementsecore_eenumliteral) {
        this.refinementsecore_eenumliteral = refinementsecore_eenumliteral;
    }
    public List<RefinementsEcore_EEnumLiteral> getRefinementsecore_eenumliterals() {
        return refinementsecore_eenumliterals;
    }

    public void addRefinementsecore_eenumliteral(Refinementsecore_eenumliteral refinementsecore_eenumliteral) {
        this.refinementsecore_eenumliterals.add(refinementsecore_eenumliteral);
    }

}