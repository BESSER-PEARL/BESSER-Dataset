





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_SetState extends PosConditionMessageExpressionElement {

    private String name;





    private Instructions_HALL_Component instructions_hall_component;


    public HALL_Instructions_SetState(
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

    public Instructions_HALL_Component getInstructions_hall_component() {
        return instructions_hall_component;
    }

    public void setInstructions_hall_component(Instructions_HALL_Component instructions_hall_component) {
        this.instructions_hall_component = instructions_hall_component;
    }

}