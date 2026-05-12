





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_SmartTagType  {

    private String url;
    private String namespaceuri;
    private String name;



    public SpreadsheetMLStyles_SmartTagType(
        String url,        String namespaceuri,        String name    ) {
        this.url = url;
        this.namespaceuri = namespaceuri;
        this.name = name;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
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


}