





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorksheetOpt_SmartTagType  {

    private String namespaceuri;
    private String name;
    private String url;





    private SmartTagsCollection smarttagscollection;


    public SpreadsheetMLWorksheetOpt_SmartTagType(
        String namespaceuri,        String name,        String url    ) {
        this.namespaceuri = namespaceuri;
        this.name = name;
        this.url = url;
    }


    public String getNamespaceuri() {
        return namespaceuri;
    }

    public void setNamespaceuri(String namespaceuri) {
        this.namespaceuri = namespaceuri;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public SmartTagsCollection getSmarttagscollection() {
        return smarttagscollection;
    }

    public void setSmarttagscollection(SmartTagsCollection smarttagscollection) {
        this.smarttagscollection = smarttagscollection;
    }

}