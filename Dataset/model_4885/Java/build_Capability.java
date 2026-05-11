





import java.util.List;
import java.util.ArrayList;

public class build_Capability extends INamedValue {

    private String nameSpace;





    private build_BExpression build_bexpression;


    public build_Capability(
        String nameSpace    ) {
        super(
        );
        this.nameSpace = nameSpace;
    }


    public String getNamespace() {
        return nameSpace;
    }

    public void setNamespace(String nameSpace) {
        this.nameSpace = nameSpace;
    }

    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }

}