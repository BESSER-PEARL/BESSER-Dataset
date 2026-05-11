





import java.util.List;
import java.util.ArrayList;

public class alf_NameExpression extends ValueSpecification, NonLiteralValueSpecification {

    private String postfixOp;
    private String id;
    private String prefixOp;



    public alf_NameExpression(
        String postfixOp,        String id,        String prefixOp    ) {
        super(
        );
        this.postfixOp = postfixOp;
        this.id = id;
        this.prefixOp = prefixOp;
    }


    public String getPostfixop() {
        return postfixOp;
    }

    public void setPostfixop(String postfixOp) {
        this.postfixOp = postfixOp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPrefixop() {
        return prefixOp;
    }

    public void setPrefixop(String prefixOp) {
        this.prefixOp = prefixOp;
    }


}