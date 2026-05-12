





import java.util.List;
import java.util.ArrayList;

public class XHTML_Optgroup extends Attrs, SelectElement {

    private String disabled;



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


}