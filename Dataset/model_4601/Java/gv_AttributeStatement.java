





import java.util.List;
import java.util.ArrayList;

public class gv_AttributeStatement extends Statement, Commentable {

    private String context;



    public gv_AttributeStatement(
        String context    ) {
        super(
        );
        this.context = context;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}