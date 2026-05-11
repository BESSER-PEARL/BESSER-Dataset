





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Photo extends Entities {

    private String name;



    public PhotosMetaModel_Photo(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}