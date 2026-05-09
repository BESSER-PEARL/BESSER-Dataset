





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_SpringRepository  {






    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_SpringRepository(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_SpringRepository(
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