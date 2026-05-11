





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_ConditionalExpression extends Expression {

    private String conector;



    public C_Expressions_ConditionalExpression(
        String conector    ) {
        super(
        );
        this.conector = conector;
    }


    public String getConector() {
        return conector;
    }

    public void setConector(String conector) {
        this.conector = conector;
    }


}