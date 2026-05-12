





import java.util.List;
import java.util.ArrayList;

public class XHTML_Input extends Attrs, Inlineforms, Focus, EMPTY {

    private String disabled;
    private String readonly;
    private String checked;
    private String type;





    private ContentTypes contenttypes;


    public XHTML_Input(
        String disabled,        String readonly,        String checked,        String type    ) {
        super(
        );
        this.disabled = disabled;
        this.readonly = readonly;
        this.checked = checked;
        this.type = type;
    }


    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getReadonly() {
        return readonly;
    }

    public void setReadonly(String readonly) {
        this.readonly = readonly;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ContentTypes getContenttypes() {
        return contenttypes;
    }

    public void setContenttypes(ContentTypes contenttypes) {
        this.contenttypes = contenttypes;
    }

}