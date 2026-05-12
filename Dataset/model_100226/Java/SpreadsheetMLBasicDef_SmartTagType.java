





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_SmartTagType  {

    private String namespaceuri;
    private String url;
    private String name;



    public SpreadsheetMLBasicDef_SmartTagType(
        String namespaceuri,        String url,        String name    ) {
        this.namespaceuri = namespaceuri;
        this.url = url;
        this.name = name;
    }


    public String getNamespaceuri() {
        return namespaceuri;
    }

    public void setNamespaceuri(String namespaceuri) {
        this.namespaceuri = namespaceuri;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}