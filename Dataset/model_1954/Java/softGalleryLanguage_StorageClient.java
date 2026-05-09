





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_StorageClient  {

    private String name;





    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_StorageClient(
        String name    ) {
        this.name = name;
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_StorageClient(
        String name        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.name = name;
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }

}