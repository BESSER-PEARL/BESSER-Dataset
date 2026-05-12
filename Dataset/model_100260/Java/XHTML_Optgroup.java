





import java.util.List;
import java.util.ArrayList;

public class XHTML_Optgroup extends SelectElement, Attrs {

    private String disabled;





    private Text text;


    public XHTML_Optgroup(
        String disabled    ) {
        super(
        );
        this.disabled = disabled;
    }


    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }

    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }

}