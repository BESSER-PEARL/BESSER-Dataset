





import java.util.List;
import java.util.ArrayList;

public class xwiki_TagsType extends LinkCollection {






    private List<xwiki_Tag> xwiki_tags;


    public xwiki_TagsType(
    ) {
        super(
        );
        this.xwiki_tags = new ArrayList<>();
    }

    public xwiki_TagsType(
        ArrayList<xwiki_Tag> xwiki_tags    ) {
        this.xwiki_tags = xwiki_tags;
    }


    public List<xwiki_Tag> getXwiki_tags() {
        return xwiki_tags;
    }

    public void addXwiki_tag(Xwiki_tag xwiki_tag) {
        this.xwiki_tags.add(xwiki_tag);
    }

}