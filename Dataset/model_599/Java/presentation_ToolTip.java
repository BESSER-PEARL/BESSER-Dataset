





import java.util.List;
import java.util.ArrayList;

public class presentation_ToolTip extends Widget {

    private String autoHide;
    private String message;
    private String group;
    private String visible;
    private String text;



    public presentation_ToolTip(
        String autoHide,        String message,        String group,        String visible,        String text    ) {
        super(
        );
        this.autoHide = autoHide;
        this.message = message;
        this.group = group;
        this.visible = visible;
        this.text = text;
    }


    public String getAutohide() {
        return autoHide;
    }

    public void setAutohide(String autoHide) {
        this.autoHide = autoHide;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}