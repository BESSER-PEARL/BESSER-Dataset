





import java.util.List;
import java.util.ArrayList;

public class expression_GlobalVarExpression extends Expression {

    private String name;



    public expression_GlobalVarExpression(
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