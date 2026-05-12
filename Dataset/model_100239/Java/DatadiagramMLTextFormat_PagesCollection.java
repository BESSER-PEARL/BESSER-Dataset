





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_PagesCollection  {






    private List<Page> pages;


    public DatadiagramMLTextFormat_PagesCollection(
    ) {
        this.pages = new ArrayList<>();
    }

    public DatadiagramMLTextFormat_PagesCollection(
        ArrayList<Page> pages    ) {
        this.pages = pages;
    }


    public List<Page> getPages() {
        return pages;
    }

    public void addPage(Page page) {
        this.pages.add(page);
    }

}