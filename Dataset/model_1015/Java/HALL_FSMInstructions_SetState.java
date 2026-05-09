





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetState extends PosConditionExpressionElement {

    private String name;



    public HALL_FSMInstructions_SetState(
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


}