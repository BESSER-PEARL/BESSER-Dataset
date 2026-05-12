





import java.util.List;
import java.util.ArrayList;

public class UML2_JoinNode extends ControlNode {

    private boolean isCombineDuplicate;





    private UML2_ValueSpecification uml2_valuespecification;


    public UML2_JoinNode(
        boolean isCombineDuplicate    ) {
        super(
        );
        this.isCombineDuplicate = isCombineDuplicate;
    }


    public boolean getIscombineduplicate() {
        return isCombineDuplicate;
    }

    public void setIscombineduplicate(boolean isCombineDuplicate) {
        this.isCombineDuplicate = isCombineDuplicate;
    }

    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }

}