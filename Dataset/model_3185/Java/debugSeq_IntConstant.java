





import java.util.List;
import java.util.ArrayList;

public class debugSeq_IntConstant extends Expression {

    private String value;



    public debugSeq_IntConstant(
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