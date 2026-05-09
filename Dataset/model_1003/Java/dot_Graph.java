





import java.util.List;
import java.util.ArrayList;

public class dot_Graph  {

    private String name;
    private boolean strict;
    private String type;





    private dot_GraphvizModel dot_graphvizmodel;


    public dot_Graph(
        String name,        boolean strict,        String type    ) {
        this.name = name;
        this.strict = strict;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dot_GraphvizModel getDot_graphvizmodel() {
        return dot_graphvizmodel;
    }

    public void setDot_graphvizmodel(dot_GraphvizModel dot_graphvizmodel) {
        this.dot_graphvizmodel = dot_graphvizmodel;
    }

}