





import java.util.List;
import java.util.ArrayList;

public class gv_Graph extends Commentable, AbstractGraph {

    private String strict;
    private String type;



    public gv_Graph(
        String strict,        String type    ) {
        super(
        );
        this.strict = strict;
        this.type = type;
    }


    public String getStrict() {
        return strict;
    }

    public void setStrict(String strict) {
        this.strict = strict;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}