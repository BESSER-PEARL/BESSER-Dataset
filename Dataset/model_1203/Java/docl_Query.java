





import java.util.List;
import java.util.ArrayList;

public class docl_Query extends ModuleElement {

    private String name;





    private docl_OclExpression docl_oclexpression;


    public docl_Query(
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

    public docl_OclExpression getDocl_oclexpression() {
        return docl_oclexpression;
    }

    public void setDocl_oclexpression(docl_OclExpression docl_oclexpression) {
        this.docl_oclexpression = docl_oclexpression;
    }

}