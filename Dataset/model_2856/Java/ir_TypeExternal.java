





import java.util.List;
import java.util.ArrayList;

public class ir_TypeExternal extends Type {

    private String scopeName;
    private String name;





    private List<ir_TaggedExpression> ir_taggedexpressions;


    public ir_TypeExternal(
        String scopeName,        String name    ) {
        super(
        );
        this.scopeName = scopeName;
        this.name = name;
        this.ir_taggedexpressions = new ArrayList<>();
    }

    public ir_TypeExternal(
        String scopeName,        String name        ArrayList<ir_TaggedExpression> ir_taggedexpressions    ) {
        this.scopeName = scopeName;
        this.name = name;
        this.ir_taggedexpressions = ir_taggedexpressions;
    }

    public String getScopename() {
        return scopeName;
    }

    public void setScopename(String scopeName) {
        this.scopeName = scopeName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ir_TaggedExpression> getIr_taggedexpressions() {
        return ir_taggedexpressions;
    }

    public void addIr_taggedexpression(Ir_taggedexpression ir_taggedexpression) {
        this.ir_taggedexpressions.add(ir_taggedexpression);
    }

}