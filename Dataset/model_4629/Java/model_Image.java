





import java.util.List;
import java.util.ArrayList;

public class model_Image extends Figure {

    private String uri;
    private String imageAlignment;



    public model_Image(
        String uri,        String imageAlignment    ) {
        super(
        );
        this.uri = uri;
        this.imageAlignment = imageAlignment;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getImagealignment() {
        return imageAlignment;
    }

    public void setImagealignment(String imageAlignment) {
        this.imageAlignment = imageAlignment;
    }


}