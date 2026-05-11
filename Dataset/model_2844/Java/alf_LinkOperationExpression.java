





import java.util.List;
import java.util.ArrayList;

public class alf_LinkOperationExpression extends SuffixExpression {

    private String kind;



    public alf_LinkOperationExpression(
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