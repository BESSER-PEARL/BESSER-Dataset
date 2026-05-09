





import java.util.List;
import java.util.ArrayList;

public class cst_TextExpression extends TemplateExpression {

    private String value;



    public cst_TextExpression(
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