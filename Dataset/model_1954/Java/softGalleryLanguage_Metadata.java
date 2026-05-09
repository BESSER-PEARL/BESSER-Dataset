





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_Metadata  {

    private String name;





    private softGalleryLanguage_AmazonFile softgallerylanguage_amazonfile;


    public softGalleryLanguage_Metadata(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softGalleryLanguage_AmazonFile getSoftgallerylanguage_amazonfile() {
        return softgallerylanguage_amazonfile;
    }

    public void setSoftgallerylanguage_amazonfile(softGalleryLanguage_AmazonFile softgallerylanguage_amazonfile) {
        this.softgallerylanguage_amazonfile = softgallerylanguage_amazonfile;
    }

}