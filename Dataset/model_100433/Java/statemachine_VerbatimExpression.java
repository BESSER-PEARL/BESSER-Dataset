





import java.util.List;
import java.util.ArrayList;

public class statemachine_VerbatimExpression extends Expression {

    private String code;



    public statemachine_VerbatimExpression(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}