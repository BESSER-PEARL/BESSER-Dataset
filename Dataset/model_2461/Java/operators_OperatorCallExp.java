





import java.util.List;
import java.util.ArrayList;

public class operators_OperatorCallExp extends OclExpression {

    private String name;



    public operators_OperatorCallExp(
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