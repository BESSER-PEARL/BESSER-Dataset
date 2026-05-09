





import java.util.List;
import java.util.ArrayList;

public class stateMachineDsl_BoolExp extends Expression {

    private String value;



    public stateMachineDsl_BoolExp(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}