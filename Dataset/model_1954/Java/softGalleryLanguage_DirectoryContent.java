





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_DirectoryContent  {

    private String name;





    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;




    private softGalleryLanguage_SegmentStructureContent softgallerylanguage_segmentstructurecontent;


    public softGalleryLanguage_DirectoryContent(
        String name    ) {
        this.name = name;
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_DirectoryContent(
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
    public softGalleryLanguage_SegmentStructureContent getSoftgallerylanguage_segmentstructurecontent() {
        return softgallerylanguage_segmentstructurecontent;
    }

    public void setSoftgallerylanguage_segmentstructurecontent(softGalleryLanguage_SegmentStructureContent softgallerylanguage_segmentstructurecontent) {
        this.softgallerylanguage_segmentstructurecontent = softgallerylanguage_segmentstructurecontent;
    }

}