





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EBooleanLiteralExp extends EPrimitiveType {

    private String booleanValue;



    public ocl_exp_EBooleanLiteralExp(
        String booleanValue    ) {
        super(
        );
        this.booleanValue = booleanValue;
    }


    public String getBooleanvalue() {
        return booleanValue;
    }

    public void setBooleanvalue(String booleanValue) {
        this.booleanValue = booleanValue;
    }


}