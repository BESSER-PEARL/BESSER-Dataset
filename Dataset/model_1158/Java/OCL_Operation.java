





import java.util.List;
import java.util.ArrayList;

public class OCL_Operation extends OclFeature {

    private String name;





    private OclExpression oclexpression;




    private OclType ocltype;


    public OCL_Operation(
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

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}