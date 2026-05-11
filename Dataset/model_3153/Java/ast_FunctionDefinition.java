





import java.util.List;
import java.util.ArrayList;

public class ast_FunctionDefinition extends CallableElement, Definition {

    private String kind;



    public ast_FunctionDefinition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}