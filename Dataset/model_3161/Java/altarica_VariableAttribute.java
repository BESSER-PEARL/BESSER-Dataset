





import java.util.List;
import java.util.ArrayList;

public class altarica_VariableAttribute  {

    private String name;





    private altarica_FlowDeclaration altarica_flowdeclaration;


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

    public altarica_FlowDeclaration getAltarica_flowdeclaration() {
        return altarica_flowdeclaration;
    }

    public void setAltarica_flowdeclaration(altarica_FlowDeclaration altarica_flowdeclaration) {
        this.altarica_flowdeclaration = altarica_flowdeclaration;
    }

}