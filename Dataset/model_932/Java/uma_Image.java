





import java.util.List;
import java.util.ArrayList;

public class uma_Image extends LeafElement {

    private String mimeType;
    private String uri;



    public uma_Image(
        String mimeType,        String uri    ) {
        super(
        );
        this.mimeType = mimeType;
        this.uri = uri;
    }


    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}