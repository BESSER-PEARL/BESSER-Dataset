





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ReactFunctions  {

    private String renderclass;
    private String lifecycleclass;





    private softGalleryLanguage_ComponentClass softgallerylanguage_componentclass;


    public softGalleryLanguage_ReactFunctions(
        String renderclass,        String lifecycleclass    ) {
        this.renderclass = renderclass;
        this.lifecycleclass = lifecycleclass;
    }


    public String getRenderclass() {
        return renderclass;
    }

    public void setRenderclass(String renderclass) {
        this.renderclass = renderclass;
    }
    public String getLifecycleclass() {
        return lifecycleclass;
    }

    public void setLifecycleclass(String lifecycleclass) {
        this.lifecycleclass = lifecycleclass;
    }

    public softGalleryLanguage_ComponentClass getSoftgallerylanguage_componentclass() {
        return softgallerylanguage_componentclass;
    }

    public void setSoftgallerylanguage_componentclass(softGalleryLanguage_ComponentClass softgallerylanguage_componentclass) {
        this.softgallerylanguage_componentclass = softgallerylanguage_componentclass;
    }

}