





import java.util.List;
import java.util.ArrayList;

public class alf_Annotation  {

    private String id;





    private alf_Annotations alf_annotations;


    public alf_Annotation(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public alf_Annotations getAlf_annotations() {
        return alf_annotations;
    }

    public void setAlf_annotations(alf_Annotations alf_annotations) {
        this.alf_annotations = alf_annotations;
    }

}