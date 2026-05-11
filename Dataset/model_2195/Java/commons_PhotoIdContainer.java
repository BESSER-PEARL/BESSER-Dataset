





import java.util.List;
import java.util.ArrayList;

public class commons_PhotoIdContainer extends Imageable {

    private String photoId;



    public commons_PhotoIdContainer(
        String photoId    ) {
        super(
        );
        this.photoId = photoId;
    }


    public String getPhotoid() {
        return photoId;
    }

    public void setPhotoid(String photoId) {
        this.photoId = photoId;
    }


}