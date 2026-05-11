





import java.util.List;
import java.util.ArrayList;

public class r1_TupleTypeSpecifier extends TypeSpecifier {






    private List<r1_TupleElementDefinition> r1_tupleelementdefinitions;


    public r1_TupleTypeSpecifier(
    ) {
        super(
        );
        this.r1_tupleelementdefinitions = new ArrayList<>();
    }

    public r1_TupleTypeSpecifier(
        ArrayList<r1_TupleElementDefinition> r1_tupleelementdefinitions    ) {
        this.r1_tupleelementdefinitions = r1_tupleelementdefinitions;
    }


    public List<r1_TupleElementDefinition> getR1_tupleelementdefinitions() {
        return r1_tupleelementdefinitions;
    }

    public void addR1_tupleelementdefinition(R1_tupleelementdefinition r1_tupleelementdefinition) {
        this.r1_tupleelementdefinitions.add(r1_tupleelementdefinition);
    }

}