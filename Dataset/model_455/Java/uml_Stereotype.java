





import java.util.List;
import java.util.ArrayList;

public class uml_Stereotype extends Class {






    private List<uml_Image> uml_images;


    public uml_Stereotype(
    ) {
        super(
        );
        this.uml_images = new ArrayList<>();
    }

    public uml_Stereotype(
        ArrayList<uml_Image> uml_images    ) {
        this.uml_images = uml_images;
    }


    public List<uml_Image> getUml_images() {
        return uml_images;
    }

    public void addUml_image(Uml_image uml_image) {
        this.uml_images.add(uml_image);
    }

}