





import java.util.List;
import java.util.ArrayList;

public class pivot_EnumerationLiteral extends InstanceSpecification {

    private String value;





    private pivot_Enumeration pivot_enumeration;




    private pivot_EnumLiteralExp pivot_enumliteralexp;




    private pivot_Enumeration pivot_enumeration;


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

    public pivot_Enumeration getPivot_enumeration() {
        return pivot_enumeration;
    }

    public void setPivot_enumeration(pivot_Enumeration pivot_enumeration) {
        this.pivot_enumeration = pivot_enumeration;
    }
    public pivot_EnumLiteralExp getPivot_enumliteralexp() {
        return pivot_enumliteralexp;
    }

    public void setPivot_enumliteralexp(pivot_EnumLiteralExp pivot_enumliteralexp) {
        this.pivot_enumliteralexp = pivot_enumliteralexp;
    }
    public pivot_Enumeration getPivot_enumeration() {
        return pivot_enumeration;
    }

    public void setPivot_enumeration(pivot_Enumeration pivot_enumeration) {
        this.pivot_enumeration = pivot_enumeration;
    }

}