





import java.util.List;
import java.util.ArrayList;

public class alf_ClassMember  {

    private String comment;





    private alf_StereotypeAnnotations alf_stereotypeannotations;




    private alf_VisibilityIndicator alf_visibilityindicator;




    private alf_ClassBody alf_classbody;


    public alf_ClassMember(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public alf_StereotypeAnnotations getAlf_stereotypeannotations() {
        return alf_stereotypeannotations;
    }

    public void setAlf_stereotypeannotations(alf_StereotypeAnnotations alf_stereotypeannotations) {
        this.alf_stereotypeannotations = alf_stereotypeannotations;
    }
    public alf_VisibilityIndicator getAlf_visibilityindicator() {
        return alf_visibilityindicator;
    }

    public void setAlf_visibilityindicator(alf_VisibilityIndicator alf_visibilityindicator) {
        this.alf_visibilityindicator = alf_visibilityindicator;
    }
    public alf_ClassBody getAlf_classbody() {
        return alf_classbody;
    }

    public void setAlf_classbody(alf_ClassBody alf_classbody) {
        this.alf_classbody = alf_classbody;
    }

}