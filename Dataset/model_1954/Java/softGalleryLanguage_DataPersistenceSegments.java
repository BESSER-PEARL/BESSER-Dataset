





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_DataPersistenceSegments  {

    private String postSName;
    private String amazonSName;





    private softGalleryLanguage_DataPersistenceContent softgallerylanguage_datapersistencecontent;


    public softGalleryLanguage_DataPersistenceSegments(
        String postSName,        String amazonSName    ) {
        this.postSName = postSName;
        this.amazonSName = amazonSName;
    }


    public String getPostsname() {
        return postSName;
    }

    public void setPostsname(String postSName) {
        this.postSName = postSName;
    }
    public String getAmazonsname() {
        return amazonSName;
    }

    public void setAmazonsname(String amazonSName) {
        this.amazonSName = amazonSName;
    }

    public softGalleryLanguage_DataPersistenceContent getSoftgallerylanguage_datapersistencecontent() {
        return softgallerylanguage_datapersistencecontent;
    }

    public void setSoftgallerylanguage_datapersistencecontent(softGalleryLanguage_DataPersistenceContent softgallerylanguage_datapersistencecontent) {
        this.softgallerylanguage_datapersistencecontent = softgallerylanguage_datapersistencecontent;
    }

}