





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_Let extends PosConditionExpression {

    private String name;





    private FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression;




    private Type type;




    private FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression;


    public HALL_FSMInstructions_Let(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FSMInstructions_PosConditionExpression getFsminstructions_posconditionexpression() {
        return fsminstructions_posconditionexpression;
    }

    public void setFsminstructions_posconditionexpression(FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression) {
        this.fsminstructions_posconditionexpression = fsminstructions_posconditionexpression;
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public FSMInstructions_PosConditionExpression getFsminstructions_posconditionexpression() {
        return fsminstructions_posconditionexpression;
    }

    public void setFsminstructions_posconditionexpression(FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression) {
        this.fsminstructions_posconditionexpression = fsminstructions_posconditionexpression;
    }

}