





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_extPHP_Button extends HTMLElement {

    private String content;
    private String type;
    private boolean disabled;



    public PHPMVC_extPHP_Button(
        String content,        String type,        boolean disabled    ) {
        super(
        );
        this.content = content;
        this.type = type;
        this.disabled = disabled;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }


}