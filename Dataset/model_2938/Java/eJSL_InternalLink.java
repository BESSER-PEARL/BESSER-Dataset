





import java.util.List;
import java.util.ArrayList;

public class eJSL_InternalLink extends Link {

    private String name;





    private eJSL_Page ejsl_page;


    public eJSL_InternalLink(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_Page getEjsl_page() {
        return ejsl_page;
    }

    public void setEjsl_page(eJSL_Page ejsl_page) {
        this.ejsl_page = ejsl_page;
    }

}