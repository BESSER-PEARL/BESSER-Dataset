





import java.util.List;
import java.util.ArrayList;

public class graphbt_Parameter  {

    private String name;
    private String type;





    private graphbt_MethodDeclaration graphbt_methoddeclaration;


    public graphbt_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public graphbt_MethodDeclaration getGraphbt_methoddeclaration() {
        return graphbt_methoddeclaration;
    }

    public void setGraphbt_methoddeclaration(graphbt_MethodDeclaration graphbt_methoddeclaration) {
        this.graphbt_methoddeclaration = graphbt_methoddeclaration;
    }

}