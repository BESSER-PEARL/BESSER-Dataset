





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Stereotype extends Class {






    private List<UMLModel_Image> umlmodel_images;


    public UMLModel_Stereotype(
    ) {
        super(
        );
        this.umlmodel_images = new ArrayList<>();
    }

    public UMLModel_Stereotype(
        ArrayList<UMLModel_Image> umlmodel_images    ) {
        this.umlmodel_images = umlmodel_images;
    }


    public List<UMLModel_Image> getUmlmodel_images() {
        return umlmodel_images;
    }

    public void addUmlmodel_image(Umlmodel_image umlmodel_image) {
        this.umlmodel_images.add(umlmodel_image);
    }

}