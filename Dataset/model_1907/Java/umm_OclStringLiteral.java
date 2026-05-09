





import java.util.List;
import java.util.ArrayList;

public class umm_OclStringLiteral extends OclLiteral {

    private String value;



    public umm_OclStringLiteral(
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