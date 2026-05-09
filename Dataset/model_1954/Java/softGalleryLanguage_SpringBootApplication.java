





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_SpringBootApplication  {






    private softGalleryLanguage_Spring softgallerylanguage_spring;




    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_SpringBootApplication(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_SpringBootApplication(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public softGalleryLanguage_Spring getSoftgallerylanguage_spring() {
        return softgallerylanguage_spring;
    }

    public void setSoftgallerylanguage_spring(softGalleryLanguage_Spring softgallerylanguage_spring) {
        this.softgallerylanguage_spring = softgallerylanguage_spring;
    }
    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }

}