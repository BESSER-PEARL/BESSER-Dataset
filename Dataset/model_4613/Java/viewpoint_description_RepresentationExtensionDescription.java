





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationExtensionDescription  {

    private String viewpointURI;
    private String representationName;
    private String name;



    public viewpoint_description_RepresentationExtensionDescription(
        String viewpointURI,        String representationName,        String name    ) {
        this.viewpointURI = viewpointURI;
        this.representationName = representationName;
        this.name = name;
    }


    public String getViewpointuri() {
        return viewpointURI;
    }

    public void setViewpointuri(String viewpointURI) {
        this.viewpointURI = viewpointURI;
    }
    public String getRepresentationname() {
        return representationName;
    }

    public void setRepresentationname(String representationName) {
        this.representationName = representationName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}