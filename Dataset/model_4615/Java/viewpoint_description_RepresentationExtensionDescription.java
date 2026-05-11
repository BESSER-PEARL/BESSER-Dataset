





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationExtensionDescription  {

    private String representationName;
    private String viewpointURI;
    private String name;





    private List<description_viewpoint_EPackage> description_viewpoint_epackages;


    public viewpoint_description_RepresentationExtensionDescription(
        String representationName,        String viewpointURI,        String name    ) {
        this.representationName = representationName;
        this.viewpointURI = viewpointURI;
        this.name = name;
        this.description_viewpoint_epackages = new ArrayList<>();
    }

    public viewpoint_description_RepresentationExtensionDescription(
        String representationName,        String viewpointURI,        String name        ArrayList<description_viewpoint_EPackage> description_viewpoint_epackages    ) {
        this.representationName = representationName;
        this.viewpointURI = viewpointURI;
        this.name = name;
        this.description_viewpoint_epackages = description_viewpoint_epackages;
    }

    public String getRepresentationname() {
        return representationName;
    }

    public void setRepresentationname(String representationName) {
        this.representationName = representationName;
    }
    public String getViewpointuri() {
        return viewpointURI;
    }

    public void setViewpointuri(String viewpointURI) {
        this.viewpointURI = viewpointURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<description_viewpoint_EPackage> getDescription_viewpoint_epackages() {
        return description_viewpoint_epackages;
    }

    public void addDescription_viewpoint_epackage(Description_viewpoint_epackage description_viewpoint_epackage) {
        this.description_viewpoint_epackages.add(description_viewpoint_epackage);
    }

}