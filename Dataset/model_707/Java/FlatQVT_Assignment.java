





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Assignment extends Element {

    private String isDefault;





    private BottomPattern bottompattern;




    private OclExpression oclexpression;


    public FlatQVT_Assignment(
        String isDefault    ) {
        super(
        );
        this.isDefault = isDefault;
    }


    public String getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(String isDefault) {
        this.isDefault = isDefault;
    }

    public BottomPattern getBottompattern() {
        return bottompattern;
    }

    public void setBottompattern(BottomPattern bottompattern) {
        this.bottompattern = bottompattern;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}