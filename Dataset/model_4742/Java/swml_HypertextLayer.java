





import java.util.List;
import java.util.ArrayList;

public class swml_HypertextLayer  {






    private List<swml_Page> swml_pages;




    private swml_WebModel swml_webmodel;




    private swml_Page swml_page;


    public swml_HypertextLayer(
    ) {
        this.swml_pages = new ArrayList<>();
    }

    public swml_HypertextLayer(
        ArrayList<swml_Page> swml_pages    ) {
        this.swml_pages = swml_pages;
    }


    public List<swml_Page> getSwml_pages() {
        return swml_pages;
    }

    public void addSwml_page(Swml_page swml_page) {
        this.swml_pages.add(swml_page);
    }
    public swml_WebModel getSwml_webmodel() {
        return swml_webmodel;
    }

    public void setSwml_webmodel(swml_WebModel swml_webmodel) {
        this.swml_webmodel = swml_webmodel;
    }
    public swml_Page getSwml_page() {
        return swml_page;
    }

    public void setSwml_page(swml_Page swml_page) {
        this.swml_page = swml_page;
    }

}