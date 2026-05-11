





import java.util.List;
import java.util.ArrayList;

public class SPL_RemoteFunctionDeclaration extends FunctionDeclaration {

    private String functionLocation;



    public SPL_RemoteFunctionDeclaration(
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