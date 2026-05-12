





import java.util.List;
import java.util.ArrayList;

public class Tag  {

    private String name;





    private ContentPage contentpage;




    private List<ContentPage> contentpages;


    public Tag(
        String name    ) {
        this.name = name;
        this.contentpages = new ArrayList<>();
    }

    public Tag(
        String name        ArrayList<ContentPage> contentpages    ) {
        this.name = name;
        this.contentpages = contentpages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ContentPage getContentpage() {
        return contentpage;
    }

    public void setContentpage(ContentPage contentpage) {
        this.contentpage = contentpage;
    }
    public List<ContentPage> getContentpages() {
        return contentpages;
    }

    public void addContentpage(Contentpage contentpage) {
        this.contentpages.add(contentpage);
    }

}