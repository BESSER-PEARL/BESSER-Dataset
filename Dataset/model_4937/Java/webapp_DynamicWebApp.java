





import java.util.List;
import java.util.ArrayList;

public class webapp_DynamicWebApp  {

    private String name;





    private List<webapp_Page> webapp_pages;


    public webapp_DynamicWebApp(
        String name    ) {
        this.name = name;
        this.webapp_pages = new ArrayList<>();
    }

    public webapp_DynamicWebApp(
        String name        ArrayList<webapp_Page> webapp_pages    ) {
        this.name = name;
        this.webapp_pages = webapp_pages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<webapp_Page> getWebapp_pages() {
        return webapp_pages;
    }

    public void addWebapp_page(Webapp_page webapp_page) {
        this.webapp_pages.add(webapp_page);
    }

}