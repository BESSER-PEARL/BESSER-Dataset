





import java.util.List;
import java.util.ArrayList;

public class swml_v2_NavigationLayer  {






    private swml_v2_WebModel swml_v2_webmodel;




    private swml_v2_Page swml_v2_page;




    private List<swml_v2_Page> swml_v2_pages;


    public swml_v2_NavigationLayer(
    ) {
        this.swml_v2_pages = new ArrayList<>();
    }

    public swml_v2_NavigationLayer(
        ArrayList<swml_v2_Page> swml_v2_pages    ) {
        this.swml_v2_pages = swml_v2_pages;
    }


    public swml_v2_WebModel getSwml_v2_webmodel() {
        return swml_v2_webmodel;
    }

    public void setSwml_v2_webmodel(swml_v2_WebModel swml_v2_webmodel) {
        this.swml_v2_webmodel = swml_v2_webmodel;
    }
    public swml_v2_Page getSwml_v2_page() {
        return swml_v2_page;
    }

    public void setSwml_v2_page(swml_v2_Page swml_v2_page) {
        this.swml_v2_page = swml_v2_page;
    }
    public List<swml_v2_Page> getSwml_v2_pages() {
        return swml_v2_pages;
    }

    public void addSwml_v2_page(Swml_v2_page swml_v2_page) {
        this.swml_v2_pages.add(swml_v2_page);
    }

}