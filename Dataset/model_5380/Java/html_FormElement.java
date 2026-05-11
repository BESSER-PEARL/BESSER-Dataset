





import java.util.List;
import java.util.ArrayList;

public class html_FormElement  {

    private boolean visible;
    private String id;





    private html_Section html_section;


    public html_FormElement(
        boolean visible,        String id    ) {
        this.visible = visible;
        this.id = id;
    }


    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public html_Section getHtml_section() {
        return html_section;
    }

    public void setHtml_section(html_Section html_section) {
        this.html_section = html_section;
    }

}