





import java.util.List;
import java.util.ArrayList;

public class form_Input extends Editable {

    private String type;
    private boolean checked;
    private String value;



    public form_Input(
        String type,        boolean checked,        String value    ) {
        super(
        );
        this.type = type;
        this.checked = checked;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getChecked() {
        return checked;
    }

    public void setChecked(boolean checked) {
        this.checked = checked;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}