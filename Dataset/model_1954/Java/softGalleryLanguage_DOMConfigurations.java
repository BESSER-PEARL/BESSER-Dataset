





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_DOMConfigurations  {

    private String name;
    private String elements;





    private softGalleryLanguage_ReactConfigurations softgallerylanguage_reactconfigurations;


    public softGalleryLanguage_DOMConfigurations(
        String name,        String elements    ) {
        this.name = name;
        this.elements = elements;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElements() {
        return elements;
    }

    public void setElements(String elements) {
        this.elements = elements;
    }

    public softGalleryLanguage_ReactConfigurations getSoftgallerylanguage_reactconfigurations() {
        return softgallerylanguage_reactconfigurations;
    }

    public void setSoftgallerylanguage_reactconfigurations(softGalleryLanguage_ReactConfigurations softgallerylanguage_reactconfigurations) {
        this.softgallerylanguage_reactconfigurations = softgallerylanguage_reactconfigurations;
    }

}