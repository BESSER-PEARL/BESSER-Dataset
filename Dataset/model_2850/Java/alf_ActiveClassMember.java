





import java.util.List;
import java.util.ArrayList;

public class alf_ActiveClassMember  {

    private String comment;





    private alf_VisibilityIndicator alf_visibilityindicator;




    private alf_StereotypeAnnotations alf_stereotypeannotations;


    public alf_ActiveClassMember(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public alf_VisibilityIndicator getAlf_visibilityindicator() {
        return alf_visibilityindicator;
    }

    public void setAlf_visibilityindicator(alf_VisibilityIndicator alf_visibilityindicator) {
        this.alf_visibilityindicator = alf_visibilityindicator;
    }
    public alf_StereotypeAnnotations getAlf_stereotypeannotations() {
        return alf_stereotypeannotations;
    }

    public void setAlf_stereotypeannotations(alf_StereotypeAnnotations alf_stereotypeannotations) {
        this.alf_stereotypeannotations = alf_stereotypeannotations;
    }

}