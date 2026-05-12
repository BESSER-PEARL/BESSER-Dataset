





import java.util.List;
import java.util.ArrayList;

public class XHTML_Select extends Attrs, Inlineforms {

    private String multiple;
    private String disabled;



    public XHTML_Select(
        String multiple,        String disabled    ) {
        super(
        );
        this.multiple = multiple;
        this.disabled = disabled;
    }


    public String getMultiple() {
        return multiple;
    }

    public void setMultiple(String multiple) {
        this.multiple = multiple;
    }
    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }


}