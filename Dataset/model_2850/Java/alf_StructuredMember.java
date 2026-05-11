





import java.util.List;
import java.util.ArrayList;

public class alf_StructuredMember  {

    private boolean isPublic;
    private String comment;





    private alf_StereotypeAnnotations alf_stereotypeannotations;




    private alf_StructuredBody alf_structuredbody;


    public alf_StructuredMember(
        boolean isPublic,        String comment    ) {
        this.isPublic = isPublic;
        this.comment = comment;
    }


    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
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
    public alf_StructuredBody getAlf_structuredbody() {
        return alf_structuredbody;
    }

    public void setAlf_structuredbody(alf_StructuredBody alf_structuredbody) {
        this.alf_structuredbody = alf_structuredbody;
    }

}