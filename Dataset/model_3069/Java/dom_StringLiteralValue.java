





import java.util.List;
import java.util.ArrayList;

public class dom_StringLiteralValue extends LiteralValue {

    private String value;





    private dom_TrimFunction dom_trimfunction;


    public dom_StringLiteralValue(
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

    public dom_TrimFunction getDom_trimfunction() {
        return dom_trimfunction;
    }

    public void setDom_trimfunction(dom_TrimFunction dom_trimfunction) {
        this.dom_trimfunction = dom_trimfunction;
    }

}