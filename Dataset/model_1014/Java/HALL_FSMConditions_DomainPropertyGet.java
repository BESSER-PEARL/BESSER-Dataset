





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMConditions_DomainPropertyGet extends PreConditionExpressionElement {

    private String name;



    public HALL_FSMConditions_DomainPropertyGet(
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