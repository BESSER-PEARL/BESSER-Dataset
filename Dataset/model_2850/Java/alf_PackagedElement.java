





import java.util.List;
import java.util.ArrayList;

public class alf_PackagedElement  {

    private String importVisibilityIndicator;
    private String comment;





    private alf_StereotypeAnnotations alf_stereotypeannotations;




    private alf_PackageBody alf_packagebody;


    public alf_PackagedElement(
        String importVisibilityIndicator,        String comment    ) {
        this.importVisibilityIndicator = importVisibilityIndicator;
        this.comment = comment;
    }


    public String getImportvisibilityindicator() {
        return importVisibilityIndicator;
    }

    public void setImportvisibilityindicator(String importVisibilityIndicator) {
        this.importVisibilityIndicator = importVisibilityIndicator;
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
    public alf_PackageBody getAlf_packagebody() {
        return alf_packagebody;
    }

    public void setAlf_packagebody(alf_PackageBody alf_packagebody) {
        this.alf_packagebody = alf_packagebody;
    }

}