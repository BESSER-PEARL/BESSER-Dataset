





import java.util.List;
import java.util.ArrayList;

public class ast_VariableDeclaration extends CallableElement, Statement {

    private String name;



    public ast_VariableDeclaration(
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