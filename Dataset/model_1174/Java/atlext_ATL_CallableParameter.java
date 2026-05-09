





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_CallableParameter  {

    private String name;





    private ATL_atlext_Type atl_atlext_type;




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

    public ATL_atlext_Type getAtl_atlext_type() {
        return atl_atlext_type;
    }

    public void setAtl_atlext_type(ATL_atlext_Type atl_atlext_type) {
        this.atl_atlext_type = atl_atlext_type;
    }
    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}