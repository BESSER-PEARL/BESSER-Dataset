





import java.util.List;
import java.util.ArrayList;

public class uma_GuidanceDescription extends ContentDescription {

    private String attachment;



    public uma_GuidanceDescription(
        String attachment    ) {
        super(
        );
        this.attachment = attachment;
    }


    public String getAttachment() {
        return attachment;
    }

    public void setAttachment(String attachment) {
        this.attachment = attachment;
    }


}