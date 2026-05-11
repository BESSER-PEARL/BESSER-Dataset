





import java.util.List;
import java.util.ArrayList;

public class ale_binding  {

    private String name;





    private ale_Expression ale_expression;


    public ale_binding(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_Expression getAle_expression() {
        return ale_expression;
    }

    public void setAle_expression(ale_Expression ale_expression) {
        this.ale_expression = ale_expression;
    }

}