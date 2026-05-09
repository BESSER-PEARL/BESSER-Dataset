





import java.util.List;
import java.util.ArrayList;

public class uma_GuidanceDescription extends ContentDescription {

    private String attachments;



    public uma_GuidanceDescription(
        String attachments    ) {
        super(
        );
        this.attachments = attachments;
    }


    public String getAttachments() {
        return attachments;
    }

    public void setAttachments(String attachments) {
        this.attachments = attachments;
    }


}