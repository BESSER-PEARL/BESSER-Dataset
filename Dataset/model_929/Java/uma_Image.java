





import java.util.List;
import java.util.ArrayList;

public class uma_Image extends LeafElement {

    private String uri;
    private String mimeType;



    public uma_Image(
        String uri,        String mimeType    ) {
        super(
        );
        this.uri = uri;
        this.mimeType = mimeType;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }


}