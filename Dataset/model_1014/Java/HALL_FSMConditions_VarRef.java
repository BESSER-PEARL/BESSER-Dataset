





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMConditions_VarRef extends PreConditionExpressionElement {

    private String name;
    private String type;



    public HALL_FSMConditions_VarRef(
        String name,        String type    ) {
        super(
        );
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}