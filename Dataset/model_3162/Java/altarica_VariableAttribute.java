





import java.util.List;
import java.util.ArrayList;

public class altarica_VariableAttribute  {

    private String name;





    private altarica_StateDeclaration altarica_statedeclaration;


    public altarica_VariableAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public altarica_StateDeclaration getAltarica_statedeclaration() {
        return altarica_statedeclaration;
    }

    public void setAltarica_statedeclaration(altarica_StateDeclaration altarica_statedeclaration) {
        this.altarica_statedeclaration = altarica_statedeclaration;
    }

}