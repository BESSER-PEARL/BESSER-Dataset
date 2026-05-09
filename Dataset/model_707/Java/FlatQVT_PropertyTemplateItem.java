





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_PropertyTemplateItem extends Element {

    private String isOpposite;





    private OclExpression oclexpression;


    public FlatQVT_PropertyTemplateItem(
        String isOpposite    ) {
        super(
        );
        this.isOpposite = isOpposite;
    }


    public String getIsopposite() {
        return isOpposite;
    }

    public void setIsopposite(String isOpposite) {
        this.isOpposite = isOpposite;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}