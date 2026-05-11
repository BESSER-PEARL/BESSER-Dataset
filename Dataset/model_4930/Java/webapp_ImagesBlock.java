





import java.util.List;
import java.util.ArrayList;

public class webapp_ImagesBlock extends Widget {

    private String imagesPath;



    public webapp_ImagesBlock(
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