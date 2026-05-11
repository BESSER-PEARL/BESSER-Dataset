





import java.util.List;
import java.util.ArrayList;

public class expressions_ast_VariableReference extends Expression {

    private String name;



    public expressions_ast_VariableReference(
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