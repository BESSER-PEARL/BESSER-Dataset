





import java.util.List;
import java.util.ArrayList;

public class gseq_Const extends IntegerExpression {

    private String value;



    public gseq_Const(
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