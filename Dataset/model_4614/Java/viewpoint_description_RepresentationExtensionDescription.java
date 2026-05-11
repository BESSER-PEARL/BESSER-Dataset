





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationExtensionDescription  {

    private String viewpointURI;
    private String name;
    private String representationName;



    public viewpoint_description_RepresentationExtensionDescription(
        String viewpointURI,        String name,        String representationName    ) {
        this.viewpointURI = viewpointURI;
        this.name = name;
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
    public String getRepresentationname() {
        return representationName;
    }

    public void setRepresentationname(String representationName) {
        this.representationName = representationName;
    }


}