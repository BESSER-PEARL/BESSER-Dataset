





import java.util.List;
import java.util.ArrayList;

public class dot_AttributeStatement extends Commentable, Statement, Attributable {

    private String context;



    public dot_AttributeStatement(
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