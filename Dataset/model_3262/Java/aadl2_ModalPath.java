





import java.util.List;
import java.util.ArrayList;

public class aadl2_ModalPath extends ModalElement {






    private List<aadl2_ModeFeature> aadl2_modefeatures;


    public aadl2_ModalPath(
    ) {
        super(
        );
        this.aadl2_modefeatures = new ArrayList<>();
    }

    public aadl2_ModalPath(
        ArrayList<aadl2_ModeFeature> aadl2_modefeatures    ) {
        this.aadl2_modefeatures = aadl2_modefeatures;
    }


    public List<aadl2_ModeFeature> getAadl2_modefeatures() {
        return aadl2_modefeatures;
    }

    public void addAadl2_modefeature(Aadl2_modefeature aadl2_modefeature) {
        this.aadl2_modefeatures.add(aadl2_modefeature);
    }

}