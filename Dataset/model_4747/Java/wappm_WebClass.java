





import java.util.List;
import java.util.ArrayList;

public class wappm_WebClass  {

    private String name;





    private wappm_ContentLayer wappm_contentlayer;




    private wappm_DynamicPage wappm_dynamicpage;


    public wappm_WebClass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wappm_ContentLayer getWappm_contentlayer() {
        return wappm_contentlayer;
    }

    public void setWappm_contentlayer(wappm_ContentLayer wappm_contentlayer) {
        this.wappm_contentlayer = wappm_contentlayer;
    }
    public wappm_DynamicPage getWappm_dynamicpage() {
        return wappm_dynamicpage;
    }

    public void setWappm_dynamicpage(wappm_DynamicPage wappm_dynamicpage) {
        this.wappm_dynamicpage = wappm_dynamicpage;
    }

}