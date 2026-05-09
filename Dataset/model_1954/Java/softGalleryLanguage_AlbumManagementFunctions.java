





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_AlbumManagementFunctions  {

    private String selectAlbName;
    private String createdAlbName;





    private softGalleryLanguage_AlbumManagement softgallerylanguage_albummanagement;


    public softGalleryLanguage_AlbumManagementFunctions(
        String selectAlbName,        String createdAlbName    ) {
        this.selectAlbName = selectAlbName;
        this.createdAlbName = createdAlbName;
    }


    public String getSelectalbname() {
        return selectAlbName;
    }

    public void setSelectalbname(String selectAlbName) {
        this.selectAlbName = selectAlbName;
    }
    public String getCreatedalbname() {
        return createdAlbName;
    }

    public void setCreatedalbname(String createdAlbName) {
        this.createdAlbName = createdAlbName;
    }

    public softGalleryLanguage_AlbumManagement getSoftgallerylanguage_albummanagement() {
        return softgallerylanguage_albummanagement;
    }

    public void setSoftgallerylanguage_albummanagement(softGalleryLanguage_AlbumManagement softgallerylanguage_albummanagement) {
        this.softgallerylanguage_albummanagement = softgallerylanguage_albummanagement;
    }

}