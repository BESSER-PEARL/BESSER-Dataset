





import java.util.List;
import java.util.ArrayList;

public class swml_Link  {

    private String href;





    private swml_StaticPage swml_staticpage;


    public swml_Link(
        String href    ) {
        this.href = href;
    }


    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }

    public swml_StaticPage getSwml_staticpage() {
        return swml_staticpage;
    }

    public void setSwml_staticpage(swml_StaticPage swml_staticpage) {
        this.swml_staticpage = swml_staticpage;
    }

}