





import java.util.List;
import java.util.ArrayList;

public class eJSL_Extension  {

    private String name;





    private eJSL_CMSExtension ejsl_cmsextension;


    public eJSL_Extension(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_CMSExtension getEjsl_cmsextension() {
        return ejsl_cmsextension;
    }

    public void setEjsl_cmsextension(eJSL_CMSExtension ejsl_cmsextension) {
        this.ejsl_cmsextension = ejsl_cmsextension;
    }

}