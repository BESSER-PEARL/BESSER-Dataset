





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetState extends PosConditionExpressionElement {

    private String name;





    private FSMInstructions_HALL_Component fsminstructions_hall_component;


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

    public FSMInstructions_HALL_Component getFsminstructions_hall_component() {
        return fsminstructions_hall_component;
    }

    public void setFsminstructions_hall_component(FSMInstructions_HALL_Component fsminstructions_hall_component) {
        this.fsminstructions_hall_component = fsminstructions_hall_component;
    }

}