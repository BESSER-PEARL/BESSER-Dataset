





import java.util.List;
import java.util.ArrayList;

public class gast_statements_LoopStatement extends Statement {

    private String kind;



    public gast_statements_LoopStatement(
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