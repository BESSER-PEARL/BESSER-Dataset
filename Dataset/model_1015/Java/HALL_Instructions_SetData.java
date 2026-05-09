





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_SetData extends PosConditionMessageExpressionElement {

    private String field;





    private Instructions_HALL_Component instructions_hall_component;


    public HALL_Instructions_SetData(
        String field    ) {
        super(
        );
        this.field = field;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public Instructions_HALL_Component getInstructions_hall_component() {
        return instructions_hall_component;
    }

    public void setInstructions_hall_component(Instructions_HALL_Component instructions_hall_component) {
        this.instructions_hall_component = instructions_hall_component;
    }

}