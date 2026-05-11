





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DAnnotationEntry extends IdentifiedElement {

    private String details;
    private String source;



    public viewpoint_description_DAnnotationEntry(
        String details,        String source    ) {
        super(
        );
        this.details = details;
        this.source = source;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}