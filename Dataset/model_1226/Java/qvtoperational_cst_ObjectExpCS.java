





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ObjectExpCS extends cst_InstantiationExpCS, cst_ElementWithBody {

    private boolean isImplicit;



    public qvtoperational_cst_ObjectExpCS(
        boolean isImplicit    ) {
        super(
        );
        this.isImplicit = isImplicit;
    }


    public boolean getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(boolean isImplicit) {
        this.isImplicit = isImplicit;
    }


}