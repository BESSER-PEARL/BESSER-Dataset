





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_PosConditionExpression  {






    private List<FSMInstructions_PosConditionExpressionElement> fsminstructions_posconditionexpressionelements;


    public HALL_FSMInstructions_PosConditionExpression(
    ) {
        this.fsminstructions_posconditionexpressionelements = new ArrayList<>();
    }

    public HALL_FSMInstructions_PosConditionExpression(
        ArrayList<FSMInstructions_PosConditionExpressionElement> fsminstructions_posconditionexpressionelements    ) {
        this.fsminstructions_posconditionexpressionelements = fsminstructions_posconditionexpressionelements;
    }


    public List<FSMInstructions_PosConditionExpressionElement> getFsminstructions_posconditionexpressionelements() {
        return fsminstructions_posconditionexpressionelements;
    }

    public void addFsminstructions_posconditionexpressionelement(Fsminstructions_posconditionexpressionelement fsminstructions_posconditionexpressionelement) {
        this.fsminstructions_posconditionexpressionelements.add(fsminstructions_posconditionexpressionelement);
    }

}