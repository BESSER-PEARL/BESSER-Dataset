





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_ImageRequirement extends OSOrImageRequirement {

    private String imageId;



    public camel_requirement_ImageRequirement(
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