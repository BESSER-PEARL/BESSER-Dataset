





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_DomainPropertyGet extends PosConditionMessageExpression {

    private String name;



    public HALL_Instructions_DomainPropertyGet(
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