





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_CallableParameter  {

    private String name;





    private VariableDeclaration variabledeclaration;


    public atlext_ATL_CallableParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}