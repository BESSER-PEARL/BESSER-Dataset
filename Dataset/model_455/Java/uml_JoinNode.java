





import java.util.List;
import java.util.ArrayList;

public class uml_JoinNode extends ControlNode {

    private String isCombineDuplicate;





    private uml_ValueSpecification uml_valuespecification;


    public uml_JoinNode(
        String isCombineDuplicate    ) {
        super(
        );
        this.isCombineDuplicate = isCombineDuplicate;
    }


    public String getIscombineduplicate() {
        return isCombineDuplicate;
    }

    public void setIscombineduplicate(String isCombineDuplicate) {
        this.isCombineDuplicate = isCombineDuplicate;
    }

    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }

}