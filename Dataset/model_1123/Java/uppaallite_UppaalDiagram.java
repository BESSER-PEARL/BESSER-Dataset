





import java.util.List;
import java.util.ArrayList;

public class uppaallite_UppaalDiagram  {

    private String declaration;
    private String resourceWeightDeclaration;



    public uppaallite_UppaalDiagram(
        String declaration,        String resourceWeightDeclaration    ) {
        this.declaration = declaration;
        this.resourceWeightDeclaration = resourceWeightDeclaration;
    }


    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getResourceweightdeclaration() {
        return resourceWeightDeclaration;
    }

    public void setResourceweightdeclaration(String resourceWeightDeclaration) {
        this.resourceWeightDeclaration = resourceWeightDeclaration;
    }


}