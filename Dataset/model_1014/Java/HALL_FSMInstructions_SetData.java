





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetData extends PosConditionExpressionElement {

    private String field;





    private FSMInstructions_HALL_Component fsminstructions_hall_component;


    public HALL_FSMInstructions_SetData(
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

    public FSMInstructions_HALL_Component getFsminstructions_hall_component() {
        return fsminstructions_hall_component;
    }

    public void setFsminstructions_hall_component(FSMInstructions_HALL_Component fsminstructions_hall_component) {
        this.fsminstructions_hall_component = fsminstructions_hall_component;
    }

}