





import java.util.List;
import java.util.ArrayList;

public class adb_AccessToDataInstance extends NotNullAccessDefinition {

    private String constant;



    public adb_AccessToDataInstance(
        String constant    ) {
        super(
        );
        this.constant = constant;
    }


    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}