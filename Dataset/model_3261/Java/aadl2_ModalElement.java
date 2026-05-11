





import java.util.List;
import java.util.ArrayList;

public class aadl2_ModalElement extends NamedElement {

    private String modesAndTransitions;



    public aadl2_ModalElement(
        String modesAndTransitions    ) {
        super(
        );
        this.modesAndTransitions = modesAndTransitions;
    }


    public String getModesandtransitions() {
        return modesAndTransitions;
    }

    public void setModesandtransitions(String modesAndTransitions) {
        this.modesAndTransitions = modesAndTransitions;
    }


}