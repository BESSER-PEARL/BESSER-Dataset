





import java.util.List;
import java.util.ArrayList;

public class UMLModel_JoinNode extends ControlNode {

    private String isCombineDuplicate;





    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_JoinNode(
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

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}