





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_AnnotationEntry  {

    private String source;





    private description_viewpoint_EObject description_viewpoint_eobject;


    public viewpoint_description_AnnotationEntry(
        String source    ) {
        this.source = source;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public description_viewpoint_EObject getDescription_viewpoint_eobject() {
        return description_viewpoint_eobject;
    }

    public void setDescription_viewpoint_eobject(description_viewpoint_EObject description_viewpoint_eobject) {
        this.description_viewpoint_eobject = description_viewpoint_eobject;
    }

}