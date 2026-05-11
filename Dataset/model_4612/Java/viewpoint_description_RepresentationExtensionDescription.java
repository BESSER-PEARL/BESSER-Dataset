





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationExtensionDescription  {

    private String representationName;
    private String viewpointURI;
    private String name;



    public viewpoint_description_RepresentationExtensionDescription(
        String representationName,        String viewpointURI,        String name    ) {
        this.representationName = representationName;
        this.viewpointURI = viewpointURI;
        this.name = name;
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


}