





import java.util.List;
import java.util.ArrayList;

public class roverml_Triggered extends Transition {

    private String operator;



    public roverml_Triggered(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}