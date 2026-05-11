





import java.util.List;
import java.util.ArrayList;

public class expressions_AddExpression extends Expression {

    private String type;



    public expressions_AddExpression(
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