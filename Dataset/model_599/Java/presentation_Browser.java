





import java.util.List;
import java.util.ArrayList;

public class presentation_Browser extends Composite {

    private String browserType;
    private String url;
    private String text;
    private String group3;





    private List<presentation_EObject> presentation_eobjects;


    public presentation_Browser(
        String browserType,        String url,        String text,        String group3    ) {
        super(
        );
        this.browserType = browserType;
        this.url = url;
        this.text = text;
        this.group3 = group3;
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_Browser(
        String browserType,        String url,        String text,        String group3        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.browserType = browserType;
        this.url = url;
        this.text = text;
        this.group3 = group3;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getBrowsertype() {
        return browserType;
    }

    public void setBrowsertype(String browserType) {
        this.browserType = browserType;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}