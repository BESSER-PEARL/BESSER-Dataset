





import java.util.List;
import java.util.ArrayList;

public class DVE_model_NumberLiteral extends Literal {

    private String value;



    public DVE_model_NumberLiteral(
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