





import java.util.List;
import java.util.ArrayList;

public class henshin_text_BoolValue extends Expression {

    private boolean value;



    public henshin_text_BoolValue(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}