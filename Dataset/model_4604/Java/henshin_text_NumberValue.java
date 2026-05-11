





import java.util.List;
import java.util.ArrayList;

public class henshin_text_NumberValue extends Expression {

    private String value;



    public henshin_text_NumberValue(
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