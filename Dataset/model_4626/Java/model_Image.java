





import java.util.List;
import java.util.ArrayList;

public class model_Image extends Figure {

    private String imageAlignment;
    private String uri;



    public model_Image(
        String imageAlignment,        String uri    ) {
        super(
        );
        this.imageAlignment = imageAlignment;
        this.uri = uri;
    }


    public String getImagealignment() {
        return imageAlignment;
    }

    public void setImagealignment(String imageAlignment) {
        this.imageAlignment = imageAlignment;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}