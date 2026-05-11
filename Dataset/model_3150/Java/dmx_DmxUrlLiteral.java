





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxUrlLiteral extends DExpression {

    private String display;
    private String value;



    public dmx_DmxUrlLiteral(
        String display,        String value    ) {
        super(
        );
        this.display = display;
        this.value = value;
    }


    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}