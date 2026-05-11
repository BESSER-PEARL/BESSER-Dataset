





import java.util.List;
import java.util.ArrayList;

public class alf_NameExpression extends NonLiteralValueSpecification, ValueSpecification {

    private String postfixOp;
    private String prefixOp;
    private String id;



    public alf_NameExpression(
        String postfixOp,        String prefixOp,        String id    ) {
        super(
        );
        this.postfixOp = postfixOp;
        this.prefixOp = prefixOp;
        this.id = id;
    }


    public String getPostfixop() {
        return postfixOp;
    }

    public void setPostfixop(String postfixOp) {
        this.postfixOp = postfixOp;
    }
    public String getPrefixop() {
        return prefixOp;
    }

    public void setPrefixop(String prefixOp) {
        this.prefixOp = prefixOp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}