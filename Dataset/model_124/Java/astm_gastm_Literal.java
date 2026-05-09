





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_Literal extends Expression {

    private String value;



    public astm_gastm_Literal(
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