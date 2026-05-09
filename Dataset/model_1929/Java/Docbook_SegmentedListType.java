





import java.util.List;
import java.util.ArrayList;

public class Docbook_SegmentedListType  {

    private String group;
    private String segtitle;





    private Docbook_RefSect1Type docbook_refsect1type;


    public Docbook_SegmentedListType(
        String group,        String segtitle    ) {
        this.group = group;
        this.segtitle = segtitle;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getSegtitle() {
        return segtitle;
    }

    public void setSegtitle(String segtitle) {
        this.segtitle = segtitle;
    }

    public Docbook_RefSect1Type getDocbook_refsect1type() {
        return docbook_refsect1type;
    }

    public void setDocbook_refsect1type(Docbook_RefSect1Type docbook_refsect1type) {
        this.docbook_refsect1type = docbook_refsect1type;
    }

}