





import java.util.List;
import java.util.ArrayList;

public class ccore_ContentItem  {






    private List<ccore_ContentItem> ccore_contentitems;




    private ccore_Item ccore_item;




    private ccore_Item ccore_item;


    public ccore_ContentItem(
    ) {
        this.ccore_contentitems = new ArrayList<>();
    }

    public ccore_ContentItem(
        ArrayList<ccore_ContentItem> ccore_contentitems    ) {
        this.ccore_contentitems = ccore_contentitems;
    }


    public List<ccore_ContentItem> getCcore_contentitems() {
        return ccore_contentitems;
    }

    public void addCcore_contentitem(Ccore_contentitem ccore_contentitem) {
        this.ccore_contentitems.add(ccore_contentitem);
    }
    public ccore_Item getCcore_item() {
        return ccore_item;
    }

    public void setCcore_item(ccore_Item ccore_item) {
        this.ccore_item = ccore_item;
    }
    public ccore_Item getCcore_item() {
        return ccore_item;
    }

    public void setCcore_item(ccore_Item ccore_item) {
        this.ccore_item = ccore_item;
    }

}