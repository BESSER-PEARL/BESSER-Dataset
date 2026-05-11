





import java.util.List;
import java.util.ArrayList;

public class commons_ThingInfo extends Imageable, Identifiable, NameContainer, Sluggable {

    private String imageId;



    public commons_ThingInfo(
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