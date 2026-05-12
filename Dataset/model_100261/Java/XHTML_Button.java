





import java.util.List;
import java.util.ArrayList;

public class XHTML_Button extends Attrs, Inlineforms, Focus {

    private String type;
    private String disabled;



    public XHTML_Button(
        String type,        String disabled    ) {
        super(
        );
        this.type = type;
        this.disabled = disabled;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }


}