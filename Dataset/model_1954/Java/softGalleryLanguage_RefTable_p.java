





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_RefTable_p  {

    private String name;





    private softGalleryLanguage_ForeignKeyRef softgallerylanguage_foreignkeyref;


    public softGalleryLanguage_RefTable_p(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softGalleryLanguage_ForeignKeyRef getSoftgallerylanguage_foreignkeyref() {
        return softgallerylanguage_foreignkeyref;
    }

    public void setSoftgallerylanguage_foreignkeyref(softGalleryLanguage_ForeignKeyRef softgallerylanguage_foreignkeyref) {
        this.softgallerylanguage_foreignkeyref = softgallerylanguage_foreignkeyref;
    }

}