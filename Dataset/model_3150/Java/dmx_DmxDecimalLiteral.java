





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxDecimalLiteral extends DExpression {

    private String value;



    public dmx_DmxDecimalLiteral(
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