





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration extends TrgFunctionDeclaration {

    private String functionLocation;



    public jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration(
        String functionLocation    ) {
        super(
        );
        this.functionLocation = functionLocation;
    }


    public String getFunctionlocation() {
        return functionLocation;
    }

    public void setFunctionlocation(String functionLocation) {
        this.functionLocation = functionLocation;
    }


}