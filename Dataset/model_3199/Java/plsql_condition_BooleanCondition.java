





import java.util.List;
import java.util.ArrayList;

public class plsql_condition_BooleanCondition extends SQLCondition {

    private String type;



    public plsql_condition_BooleanCondition(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}