





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DynamicValue extends ThreadSensitive {

    private String text;
    private String type;



    public core_actionstep_DynamicValue(
        String text,        String type    ) {
        super(
        );
        this.text = text;
        this.type = type;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}