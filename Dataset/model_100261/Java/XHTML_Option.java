





import java.util.List;
import java.util.ArrayList;

public class XHTML_Option extends Attrs, PCDATA, SelectElement {

    private String disabled;
    private String selected;



    public XHTML_Option(
        String disabled,        String selected    ) {
        super(
        );
        this.disabled = disabled;
        this.selected = selected;
    }


    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }


}