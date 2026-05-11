





import java.util.List;
import java.util.ArrayList;

public class aS3_NumberConstant extends Expression {

    private String value;



    public aS3_NumberConstant(
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