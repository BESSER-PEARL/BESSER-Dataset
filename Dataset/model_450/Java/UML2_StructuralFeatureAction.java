





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuralFeatureAction extends Action {






    private UML2_InputPin uml2_inputpin;




    private UML2_StructuralFeature uml2_structuralfeature;


    public UML2_StructuralFeatureAction(
    ) {
        super(
        );
    }



    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }
    public UML2_StructuralFeature getUml2_structuralfeature() {
        return uml2_structuralfeature;
    }

    public void setUml2_structuralfeature(UML2_StructuralFeature uml2_structuralfeature) {
        this.uml2_structuralfeature = uml2_structuralfeature;
    }

}