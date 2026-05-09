





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_VariableDeclaration extends LocatedElement {

    private String varName;



    public QualityMetamodel_QMM_OCL_VariableDeclaration(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}