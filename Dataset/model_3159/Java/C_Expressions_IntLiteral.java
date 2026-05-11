





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_IntLiteral extends Literal {

    private String value;



    public C_Expressions_IntLiteral(
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