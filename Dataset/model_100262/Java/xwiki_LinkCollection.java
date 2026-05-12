





import java.util.List;
import java.util.ArrayList;

public class xwiki_LinkCollection  {






    private List<xwiki_Link> xwiki_links;


    public xwiki_LinkCollection(
    ) {
        this.xwiki_links = new ArrayList<>();
    }

    public xwiki_LinkCollection(
        ArrayList<xwiki_Link> xwiki_links    ) {
        this.xwiki_links = xwiki_links;
    }


    public List<xwiki_Link> getXwiki_links() {
        return xwiki_links;
    }

    public void addXwiki_link(Xwiki_link xwiki_link) {
        this.xwiki_links.add(xwiki_link);
    }

}