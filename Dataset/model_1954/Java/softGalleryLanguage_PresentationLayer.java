





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_PresentationLayer  {






    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_PresentationLayer(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_PresentationLayer(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }

}