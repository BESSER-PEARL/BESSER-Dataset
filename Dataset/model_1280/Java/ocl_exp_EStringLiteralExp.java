





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EStringLiteralExp extends EPrimitiveType {

    private String stringValue;



    public ocl_exp_EStringLiteralExp(
        String stringValue    ) {
        super(
        );
        this.stringValue = stringValue;
    }


    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }


}