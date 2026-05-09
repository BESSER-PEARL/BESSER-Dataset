





import java.util.List;
import java.util.ArrayList;

public class webapp_Style extends NamedElement {

    private String src;
    private String href;





    private webapp_Template webapp_template;


    public webapp_Style(
        String src,        String href    ) {
        super(
        );
        this.src = src;
        this.href = href;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }

    public webapp_Template getWebapp_template() {
        return webapp_template;
    }

    public void setWebapp_template(webapp_Template webapp_template) {
        this.webapp_template = webapp_template;
    }

}