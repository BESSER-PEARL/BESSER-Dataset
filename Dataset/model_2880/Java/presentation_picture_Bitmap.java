





import java.util.List;
import java.util.ArrayList;

public class presentation_picture_Bitmap extends Graphic2D {

    private String bitmap_parameters;



    public presentation_picture_Bitmap(
        String bitmap_parameters    ) {
        super(
        );
        this.bitmap_parameters = bitmap_parameters;
    }


    public String getBitmap_parameters() {
        return bitmap_parameters;
    }

    public void setBitmap_parameters(String bitmap_parameters) {
        this.bitmap_parameters = bitmap_parameters;
    }


}