





import java.util.List;
import java.util.ArrayList;

public class edu_FunctionDeclaration extends ASTNode {

    private String name;



    public edu_FunctionDeclaration(
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