





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramExtensionDescription extends RepresentationExtensionDescription {






    private List<AdditionalLayer> additionallayers;




    private validation_ValidationSet validation_validationset;


    public diagram_description_DiagramExtensionDescription(
    ) {
        super(
        );
        this.additionallayers = new ArrayList<>();
    }

    public diagram_description_DiagramExtensionDescription(
        ArrayList<AdditionalLayer> additionallayers    ) {
        this.additionallayers = additionallayers;
    }


    public List<AdditionalLayer> getAdditionallayers() {
        return additionallayers;
    }

    public void addAdditionallayer(Additionallayer additionallayer) {
        this.additionallayers.add(additionallayer);
    }
    public validation_ValidationSet getValidation_validationset() {
        return validation_validationset;
    }

    public void setValidation_validationset(validation_ValidationSet validation_validationset) {
        this.validation_validationset = validation_validationset;
    }

}