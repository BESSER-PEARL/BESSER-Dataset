





import java.util.List;
import java.util.ArrayList;

public class presentation_XMLDataProvider extends AbstractDataProvider {

    private String xPath;
    private String group1;





    private List<presentation_URL> presentation_urls;


    public presentation_XMLDataProvider(
        String xPath,        String group1    ) {
        super(
        );
        this.xPath = xPath;
        this.group1 = group1;
        this.presentation_urls = new ArrayList<>();
    }

    public presentation_XMLDataProvider(
        String xPath,        String group1        ArrayList<presentation_URL> presentation_urls    ) {
        this.xPath = xPath;
        this.group1 = group1;
        this.presentation_urls = presentation_urls;
    }

    public String getXpath() {
        return xPath;
    }

    public void setXpath(String xPath) {
        this.xPath = xPath;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_URL> getPresentation_urls() {
        return presentation_urls;
    }

    public void addPresentation_url(Presentation_url presentation_url) {
        this.presentation_urls.add(presentation_url);
    }

}