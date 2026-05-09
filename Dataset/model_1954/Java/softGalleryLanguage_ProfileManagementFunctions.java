





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ProfileManagementFunctions  {

    private String viewprofileName;
    private String editProfileName;





    private softGalleryLanguage_ProfileManagement softgallerylanguage_profilemanagement;


    public softGalleryLanguage_ProfileManagementFunctions(
        String viewprofileName,        String editProfileName    ) {
        this.viewprofileName = viewprofileName;
        this.editProfileName = editProfileName;
    }


    public String getViewprofilename() {
        return viewprofileName;
    }

    public void setViewprofilename(String viewprofileName) {
        this.viewprofileName = viewprofileName;
    }
    public String getEditprofilename() {
        return editProfileName;
    }

    public void setEditprofilename(String editProfileName) {
        this.editProfileName = editProfileName;
    }

    public softGalleryLanguage_ProfileManagement getSoftgallerylanguage_profilemanagement() {
        return softgallerylanguage_profilemanagement;
    }

    public void setSoftgallerylanguage_profilemanagement(softGalleryLanguage_ProfileManagement softgallerylanguage_profilemanagement) {
        this.softgallerylanguage_profilemanagement = softgallerylanguage_profilemanagement;
    }

}