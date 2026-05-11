





import java.util.List;
import java.util.ArrayList;

public class gremlin_MethodDeclaration extends Instruction {

    private String name;
    private String parameters;



    public gremlin_MethodDeclaration(
        String name,        String parameters    ) {
        super(
        );
        this.name = name;
        this.parameters = parameters;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }


}