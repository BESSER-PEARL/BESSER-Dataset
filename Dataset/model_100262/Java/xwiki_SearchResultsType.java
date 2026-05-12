





import java.util.List;
import java.util.ArrayList;

public class xwiki_SearchResultsType extends LinkCollection {

    private String template;





    private List<xwiki_SearchResult> xwiki_searchresults;


    public xwiki_SearchResultsType(
        String template    ) {
        super(
        );
        this.template = template;
        this.xwiki_searchresults = new ArrayList<>();
    }

    public xwiki_SearchResultsType(
        String template        ArrayList<xwiki_SearchResult> xwiki_searchresults    ) {
        this.template = template;
        this.xwiki_searchresults = xwiki_searchresults;
    }

    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }

    public List<xwiki_SearchResult> getXwiki_searchresults() {
        return xwiki_searchresults;
    }

    public void addXwiki_searchresult(Xwiki_searchresult xwiki_searchresult) {
        this.xwiki_searchresults.add(xwiki_searchresult);
    }

}