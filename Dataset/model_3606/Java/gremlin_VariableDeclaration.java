





import java.util.List;
import java.util.ArrayList;

public class gremlin_VariableDeclaration extends Instruction {

    private String name;
    private boolean final;





    private gremlin_TypeDeclaration gremlin_typedeclaration;


    public gremlin_VariableDeclaration(
        String name,        boolean final    ) {
        super(
        );
        this.name = name;
        this.final = final;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public gremlin_TypeDeclaration getGremlin_typedeclaration() {
        return gremlin_typedeclaration;
    }

    public void setGremlin_typedeclaration(gremlin_TypeDeclaration gremlin_typedeclaration) {
        this.gremlin_typedeclaration = gremlin_typedeclaration;
    }

}