





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_GetData extends ActionMessageExpressionElement {

    private String field;





    private Actions_HALL_Component actions_hall_component;


    public HALL_Actions_GetData(
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

    public Actions_HALL_Component getActions_hall_component() {
        return actions_hall_component;
    }

    public void setActions_hall_component(Actions_HALL_Component actions_hall_component) {
        this.actions_hall_component = actions_hall_component;
    }

}