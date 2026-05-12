





import java.util.List;
import java.util.ArrayList;

public class XHTML_Textarea extends Attrs, Inlineforms, PCDATA, Focus {

    private String readonly;
    private String disabled;



    public XHTML_Textarea(
        String readonly,        String disabled    ) {
        super(
        );
        this.readonly = readonly;
        this.disabled = disabled;
    }


    public String getReadonly() {
        return readonly;
    }

    public void setReadonly(String readonly) {
        this.readonly = readonly;
    }
    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }


}