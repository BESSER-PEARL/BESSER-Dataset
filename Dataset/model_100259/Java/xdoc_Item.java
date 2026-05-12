





import java.util.List;
import java.util.ArrayList;

public class xdoc_Item  {






    private xdoc_UnorderedList xdoc_unorderedlist;




    private List<xdoc_TextOrMarkup> xdoc_textormarkups;




    private xdoc_OrderedList xdoc_orderedlist;


    public xdoc_Item(
    ) {
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_Item(
        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.xdoc_textormarkups = xdoc_textormarkups;
    }


    public xdoc_UnorderedList getXdoc_unorderedlist() {
        return xdoc_unorderedlist;
    }

    public void setXdoc_unorderedlist(xdoc_UnorderedList xdoc_unorderedlist) {
        this.xdoc_unorderedlist = xdoc_unorderedlist;
    }
    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }
    public xdoc_OrderedList getXdoc_orderedlist() {
        return xdoc_orderedlist;
    }

    public void setXdoc_orderedlist(xdoc_OrderedList xdoc_orderedlist) {
        this.xdoc_orderedlist = xdoc_orderedlist;
    }

}