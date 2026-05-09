





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Model extends Package {

    private String viewpoint;



    public UMLModel_Model(
        String viewpoint    ) {
        super(
        );
        this.viewpoint = viewpoint;
    }


    public String getViewpoint() {
        return viewpoint;
    }

    public void setViewpoint(String viewpoint) {
        this.viewpoint = viewpoint;
    }


}