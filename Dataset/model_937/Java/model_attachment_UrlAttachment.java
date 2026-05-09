





import java.util.List;
import java.util.ArrayList;

public class model_attachment_UrlAttachment extends Attachment {

    private String url;



    public model_attachment_UrlAttachment(
        String url    ) {
        super(
        );
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}