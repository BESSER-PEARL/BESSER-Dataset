





import java.util.List;
import java.util.ArrayList;

public class xwiki_WikisType extends LinkCollection {






    private List<xwiki_Wiki> xwiki_wikis;


    public xwiki_WikisType(
    ) {
        super(
        );
        this.xwiki_wikis = new ArrayList<>();
    }

    public xwiki_WikisType(
        ArrayList<xwiki_Wiki> xwiki_wikis    ) {
        this.xwiki_wikis = xwiki_wikis;
    }


    public List<xwiki_Wiki> getXwiki_wikis() {
        return xwiki_wikis;
    }

    public void addXwiki_wiki(Xwiki_wiki xwiki_wiki) {
        this.xwiki_wikis.add(xwiki_wiki);
    }

}