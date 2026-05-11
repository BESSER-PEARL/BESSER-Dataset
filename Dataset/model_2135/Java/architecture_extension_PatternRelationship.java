





import java.util.List;
import java.util.ArrayList;

public class architecture_extension_PatternRelationship extends Relationship {

    private String referenceName;



    public architecture_extension_PatternRelationship(
        String referenceName    ) {
        super(
        );
        this.referenceName = referenceName;
    }


    public String getReferencename() {
        return referenceName;
    }

    public void setReferencename(String referenceName) {
        this.referenceName = referenceName;
    }


}