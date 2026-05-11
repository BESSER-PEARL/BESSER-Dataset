





import java.util.List;
import java.util.ArrayList;

public class aadl2_Mode extends ModeFeature {

    private String derived;
    private String initial;





    private aadl2_ModalElement aadl2_modalelement;




    private aadl2_ModeBinding aadl2_modebinding;




    private aadl2_ModeBinding aadl2_modebinding;


    public aadl2_Mode(
        String derived,        String initial    ) {
        super(
        );
        this.derived = derived;
        this.initial = initial;
    }


    public String getDerived() {
        return derived;
    }

    public void setDerived(String derived) {
        this.derived = derived;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }

    public aadl2_ModalElement getAadl2_modalelement() {
        return aadl2_modalelement;
    }

    public void setAadl2_modalelement(aadl2_ModalElement aadl2_modalelement) {
        this.aadl2_modalelement = aadl2_modalelement;
    }
    public aadl2_ModeBinding getAadl2_modebinding() {
        return aadl2_modebinding;
    }

    public void setAadl2_modebinding(aadl2_ModeBinding aadl2_modebinding) {
        this.aadl2_modebinding = aadl2_modebinding;
    }
    public aadl2_ModeBinding getAadl2_modebinding() {
        return aadl2_modebinding;
    }

    public void setAadl2_modebinding(aadl2_ModeBinding aadl2_modebinding) {
        this.aadl2_modebinding = aadl2_modebinding;
    }

}