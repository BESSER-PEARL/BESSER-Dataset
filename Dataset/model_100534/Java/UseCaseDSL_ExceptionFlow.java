





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_ExceptionFlow extends NamedFlow {

    private String condition;



    public UseCaseDSL_ExceptionFlow(
        String condition    ) {
        super(
        );
        this.condition = condition;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}