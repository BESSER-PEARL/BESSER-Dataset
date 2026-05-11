





import java.util.List;
import java.util.ArrayList;

public class eJSL_PageReference  {

    private String sect;





    private eJSL_Section ejsl_section;




    private eJSL_Module ejsl_module;




    private eJSL_Page ejsl_page;


    public eJSL_PageReference(
        String sect    ) {
        this.sect = sect;
    }


    public String getSect() {
        return sect;
    }

    public void setSect(String sect) {
        this.sect = sect;
    }

    public eJSL_Section getEjsl_section() {
        return ejsl_section;
    }

    public void setEjsl_section(eJSL_Section ejsl_section) {
        this.ejsl_section = ejsl_section;
    }
    public eJSL_Module getEjsl_module() {
        return ejsl_module;
    }

    public void setEjsl_module(eJSL_Module ejsl_module) {
        this.ejsl_module = ejsl_module;
    }
    public eJSL_Page getEjsl_page() {
        return ejsl_page;
    }

    public void setEjsl_page(eJSL_Page ejsl_page) {
        this.ejsl_page = ejsl_page;
    }

}