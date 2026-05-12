





import java.util.List;
import java.util.ArrayList;

public class xwiki_Space extends LinkCollection {

    private String xwikiAbsoluteUrl;
    private String wiki;
    private String xwikiRelativeUrl;
    private String name;
    private String home;
    private String id;





    private xwiki_SpacesType xwiki_spacestype;


    public xwiki_Space(
        String xwikiAbsoluteUrl,        String wiki,        String xwikiRelativeUrl,        String name,        String home,        String id    ) {
        super(
        );
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
        this.wiki = wiki;
        this.xwikiRelativeUrl = xwikiRelativeUrl;
        this.name = name;
        this.home = home;
        this.id = id;
    }


    public String getXwikiabsoluteurl() {
        return xwikiAbsoluteUrl;
    }

    public void setXwikiabsoluteurl(String xwikiAbsoluteUrl) {
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
    }
    public String getWiki() {
        return wiki;
    }

    public void setWiki(String wiki) {
        this.wiki = wiki;
    }
    public String getXwikirelativeurl() {
        return xwikiRelativeUrl;
    }

    public void setXwikirelativeurl(String xwikiRelativeUrl) {
        this.xwikiRelativeUrl = xwikiRelativeUrl;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHome() {
        return home;
    }

    public void setHome(String home) {
        this.home = home;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xwiki_SpacesType getXwiki_spacestype() {
        return xwiki_spacestype;
    }

    public void setXwiki_spacestype(xwiki_SpacesType xwiki_spacestype) {
        this.xwiki_spacestype = xwiki_spacestype;
    }

}