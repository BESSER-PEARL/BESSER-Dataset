





import java.util.List;
import java.util.ArrayList;

public class emig_setterDef extends LocatedElement {

    private String operator;



    public emig_setterDef(
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