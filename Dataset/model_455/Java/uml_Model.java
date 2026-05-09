





import java.util.List;
import java.util.ArrayList;

public class uml_Model extends Package {

    private String viewpoint;



    public uml_Model(
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