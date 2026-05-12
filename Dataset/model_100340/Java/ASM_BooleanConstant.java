





import java.util.List;
import java.util.ArrayList;

public class ASM_BooleanConstant extends Constant {

    private String value;



    public ASM_BooleanConstant(
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