





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ReactSubModules  {






    private List<softGalleryLanguage_ReactComponents> softgallerylanguage_reactcomponentss;




    private softGalleryLanguage_ReactModules softgallerylanguage_reactmodules;


    public softGalleryLanguage_ReactSubModules(
    ) {
        this.softgallerylanguage_reactcomponentss = new ArrayList<>();
    }

    public softGalleryLanguage_ReactSubModules(
        ArrayList<softGalleryLanguage_ReactComponents> softgallerylanguage_reactcomponentss    ) {
        this.softgallerylanguage_reactcomponentss = softgallerylanguage_reactcomponentss;
    }


    public List<softGalleryLanguage_ReactComponents> getSoftgallerylanguage_reactcomponentss() {
        return softgallerylanguage_reactcomponentss;
    }

    public void addSoftgallerylanguage_reactcomponents(Softgallerylanguage_reactcomponents softgallerylanguage_reactcomponents) {
        this.softgallerylanguage_reactcomponentss.add(softgallerylanguage_reactcomponents);
    }
    public softGalleryLanguage_ReactModules getSoftgallerylanguage_reactmodules() {
        return softgallerylanguage_reactmodules;
    }

    public void setSoftgallerylanguage_reactmodules(softGalleryLanguage_ReactModules softgallerylanguage_reactmodules) {
        this.softgallerylanguage_reactmodules = softgallerylanguage_reactmodules;
    }

}