





import java.util.List;
import java.util.ArrayList;

public class presentation_picture_Picture extends Stimulus {






    private List<PictureParameter> pictureparameters;


    public presentation_picture_Picture(
    ) {
        super(
        );
        this.pictureparameters = new ArrayList<>();
    }

    public presentation_picture_Picture(
        ArrayList<PictureParameter> pictureparameters    ) {
        this.pictureparameters = pictureparameters;
    }


    public List<PictureParameter> getPictureparameters() {
        return pictureparameters;
    }

    public void addPictureparameter(Pictureparameter pictureparameter) {
        this.pictureparameters.add(pictureparameter);
    }

}