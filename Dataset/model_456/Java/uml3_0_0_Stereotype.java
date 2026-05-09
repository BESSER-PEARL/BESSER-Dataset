





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Stereotype extends Class {






    private List<uml3_0_0_Image> uml3_0_0_images;


    public uml3_0_0_Stereotype(
    ) {
        super(
        );
        this.uml3_0_0_images = new ArrayList<>();
    }

    public uml3_0_0_Stereotype(
        ArrayList<uml3_0_0_Image> uml3_0_0_images    ) {
        this.uml3_0_0_images = uml3_0_0_images;
    }


    public List<uml3_0_0_Image> getUml3_0_0_images() {
        return uml3_0_0_images;
    }

    public void addUml3_0_0_image(Uml3_0_0_image uml3_0_0_image) {
        this.uml3_0_0_images.add(uml3_0_0_image);
    }

}