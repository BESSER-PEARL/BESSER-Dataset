





import java.util.List;
import java.util.ArrayList;

public class dot_Graph extends Commentable, AbstractGraph {

    private String type;
    private String strict;



    public dot_Graph(
        String type,        String strict    ) {
        super(
        );
        this.type = type;
        this.strict = strict;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStrict() {
        return strict;
    }

    public void setStrict(String strict) {
        this.strict = strict;
    }


}