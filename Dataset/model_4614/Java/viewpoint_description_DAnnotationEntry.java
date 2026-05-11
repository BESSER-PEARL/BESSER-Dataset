





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DAnnotationEntry  {

    private String source;
    private String details;



    public viewpoint_description_DAnnotationEntry(
        String source,        String details    ) {
        this.source = source;
        this.details = details;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }


}