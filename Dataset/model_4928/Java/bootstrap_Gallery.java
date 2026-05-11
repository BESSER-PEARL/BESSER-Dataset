





import java.util.List;
import java.util.ArrayList;

public class bootstrap_Gallery extends Widget {

    private String imagesPath;



    public bootstrap_Gallery(
        String imagesPath    ) {
        super(
        );
        this.imagesPath = imagesPath;
    }


    public String getImagespath() {
        return imagesPath;
    }

    public void setImagespath(String imagesPath) {
        this.imagesPath = imagesPath;
    }


}