





import java.util.List;
import java.util.ArrayList;

public class pivot_EnumerationLiteral extends NamedElement {

    private String value;





    private pivot_EnumLiteralExp pivot_enumliteralexp;


    public pivot_EnumerationLiteral(
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

    public pivot_EnumLiteralExp getPivot_enumliteralexp() {
        return pivot_enumliteralexp;
    }

    public void setPivot_enumliteralexp(pivot_EnumLiteralExp pivot_enumliteralexp) {
        this.pivot_enumliteralexp = pivot_enumliteralexp;
    }

}