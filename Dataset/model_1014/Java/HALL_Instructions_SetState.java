





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_SetState extends PosConditionMessageExpressionElement {

    private String name;



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


}