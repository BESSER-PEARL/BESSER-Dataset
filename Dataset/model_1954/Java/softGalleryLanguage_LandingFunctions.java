





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_LandingFunctions  {

    private String passPhotoName;
    private String nameCarouselName;





    private softGalleryLanguage_LandingActions softgallerylanguage_landingactions;


    public softGalleryLanguage_LandingFunctions(
        String passPhotoName,        String nameCarouselName    ) {
        this.passPhotoName = passPhotoName;
        this.nameCarouselName = nameCarouselName;
    }


    public String getPassphotoname() {
        return passPhotoName;
    }

    public void setPassphotoname(String passPhotoName) {
        this.passPhotoName = passPhotoName;
    }
    public String getNamecarouselname() {
        return nameCarouselName;
    }

    public void setNamecarouselname(String nameCarouselName) {
        this.nameCarouselName = nameCarouselName;
    }

    public softGalleryLanguage_LandingActions getSoftgallerylanguage_landingactions() {
        return softgallerylanguage_landingactions;
    }

    public void setSoftgallerylanguage_landingactions(softGalleryLanguage_LandingActions softgallerylanguage_landingactions) {
        this.softgallerylanguage_landingactions = softgallerylanguage_landingactions;
    }

}