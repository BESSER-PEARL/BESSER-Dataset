





import java.util.List;
import java.util.ArrayList;

public class model_Image extends ConnectableElement {

    private String imageId;



    public model_Image(
        String imageId    ) {
        super(
        );
        this.imageId = imageId;
    }


    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }


}