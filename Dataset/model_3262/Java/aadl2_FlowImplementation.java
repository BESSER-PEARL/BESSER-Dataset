





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowImplementation extends ModalPath, ClassifierFeature, Flow {

    private String kind;



    public aadl2_FlowImplementation(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}