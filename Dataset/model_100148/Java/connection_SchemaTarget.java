





import java.util.List;
import java.util.ArrayList;

public class connection_SchemaTarget  {

    private String RelativeXPathQuery;
    private String TagName;



    public connection_SchemaTarget(
        String RelativeXPathQuery,        String TagName    ) {
        this.RelativeXPathQuery = RelativeXPathQuery;
        this.TagName = TagName;
    }


    public String getRelativexpathquery() {
        return RelativeXPathQuery;
    }

    public void setRelativexpathquery(String RelativeXPathQuery) {
        this.RelativeXPathQuery = RelativeXPathQuery;
    }
    public String getTagname() {
        return TagName;
    }

    public void setTagname(String TagName) {
        this.TagName = TagName;
    }


}