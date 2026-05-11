





import java.util.List;
import java.util.ArrayList;

public class types_Case extends Element {

    private String literal;





    private types_Branch types_branch;


    public types_Case(
        String literal    ) {
        super(
        );
        this.literal = literal;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }

    public types_Branch getTypes_branch() {
        return types_branch;
    }

    public void setTypes_branch(types_Branch types_branch) {
        this.types_branch = types_branch;
    }

}