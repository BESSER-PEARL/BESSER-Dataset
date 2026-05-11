





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgStructureProperty extends TrgLocatedElement {

    private String name;





    private TrgTypeExpression trgtypeexpression;


    public jointPackage_CPL2SPL_TrgStructureProperty(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TrgTypeExpression getTrgtypeexpression() {
        return trgtypeexpression;
    }

    public void setTrgtypeexpression(TrgTypeExpression trgtypeexpression) {
        this.trgtypeexpression = trgtypeexpression;
    }

}