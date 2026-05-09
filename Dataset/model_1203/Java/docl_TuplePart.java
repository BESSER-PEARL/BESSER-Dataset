





import java.util.List;
import java.util.ArrayList;

public class docl_TuplePart  {

    private String name;





    private docl_OclExpression docl_oclexpression;




    private docl_OclType docl_ocltype;


    public docl_TuplePart(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public docl_OclExpression getDocl_oclexpression() {
        return docl_oclexpression;
    }

    public void setDocl_oclexpression(docl_OclExpression docl_oclexpression) {
        this.docl_oclexpression = docl_oclexpression;
    }
    public docl_OclType getDocl_ocltype() {
        return docl_ocltype;
    }

    public void setDocl_ocltype(docl_OclType docl_ocltype) {
        this.docl_ocltype = docl_ocltype;
    }

}