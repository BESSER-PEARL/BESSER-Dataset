





import java.util.List;
import java.util.ArrayList;

public class logo_expression_VariableRead extends Expression {

    private String name;



    public logo_expression_VariableRead(
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