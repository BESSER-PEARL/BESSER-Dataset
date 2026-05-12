





import java.util.List;
import java.util.ArrayList;

public class xwiki_Object extends ObjectSummary {






    private xwiki_DocumentRoot xwiki_documentroot;




    private xwiki_SearchResult xwiki_searchresult;




    private List<xwiki_Property> xwiki_propertys;


    public xwiki_Object(
    ) {
        super(
        );
        this.xwiki_propertys = new ArrayList<>();
    }

    public xwiki_Object(
        ArrayList<xwiki_Property> xwiki_propertys    ) {
        this.xwiki_propertys = xwiki_propertys;
    }


    public xwiki_DocumentRoot getXwiki_documentroot() {
        return xwiki_documentroot;
    }

    public void setXwiki_documentroot(xwiki_DocumentRoot xwiki_documentroot) {
        this.xwiki_documentroot = xwiki_documentroot;
    }
    public xwiki_SearchResult getXwiki_searchresult() {
        return xwiki_searchresult;
    }

    public void setXwiki_searchresult(xwiki_SearchResult xwiki_searchresult) {
        this.xwiki_searchresult = xwiki_searchresult;
    }
    public List<xwiki_Property> getXwiki_propertys() {
        return xwiki_propertys;
    }

    public void addXwiki_property(Xwiki_property xwiki_property) {
        this.xwiki_propertys.add(xwiki_property);
    }

}