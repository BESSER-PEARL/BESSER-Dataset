





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Methods extends BlockStatement {

    private String methodName;



    public gast_statements_Methods(
        String methodName    ) {
        super(
        );
        this.methodName = methodName;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }


}