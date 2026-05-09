





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_Clause  {

    private String name;





    private softGalleryLanguage_Query softgallerylanguage_query;


    public softGalleryLanguage_Clause(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softGalleryLanguage_Query getSoftgallerylanguage_query() {
        return softgallerylanguage_query;
    }

    public void setSoftgallerylanguage_query(softGalleryLanguage_Query softgallerylanguage_query) {
        this.softgallerylanguage_query = softgallerylanguage_query;
    }

}