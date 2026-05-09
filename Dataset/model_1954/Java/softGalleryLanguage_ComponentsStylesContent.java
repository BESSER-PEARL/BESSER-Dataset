





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ComponentsStylesContent  {

    private String nameStyle;





    private List<softGalleryLanguage_StyleProperties> softgallerylanguage_stylepropertiess;




    private softGalleryLanguage_ComponentsStyles softgallerylanguage_componentsstyles;


    public softGalleryLanguage_ComponentsStylesContent(
        String nameStyle    ) {
        this.nameStyle = nameStyle;
        this.softgallerylanguage_stylepropertiess = new ArrayList<>();
    }

    public softGalleryLanguage_ComponentsStylesContent(
        String nameStyle        ArrayList<softGalleryLanguage_StyleProperties> softgallerylanguage_stylepropertiess    ) {
        this.nameStyle = nameStyle;
        this.softgallerylanguage_stylepropertiess = softgallerylanguage_stylepropertiess;
    }

    public String getNamestyle() {
        return nameStyle;
    }

    public void setNamestyle(String nameStyle) {
        this.nameStyle = nameStyle;
    }

    public List<softGalleryLanguage_StyleProperties> getSoftgallerylanguage_stylepropertiess() {
        return softgallerylanguage_stylepropertiess;
    }

    public void addSoftgallerylanguage_styleproperties(Softgallerylanguage_styleproperties softgallerylanguage_styleproperties) {
        this.softgallerylanguage_stylepropertiess.add(softgallerylanguage_styleproperties);
    }
    public softGalleryLanguage_ComponentsStyles getSoftgallerylanguage_componentsstyles() {
        return softgallerylanguage_componentsstyles;
    }

    public void setSoftgallerylanguage_componentsstyles(softGalleryLanguage_ComponentsStyles softgallerylanguage_componentsstyles) {
        this.softgallerylanguage_componentsstyles = softgallerylanguage_componentsstyles;
    }

}