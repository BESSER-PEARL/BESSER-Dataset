





import java.util.List;
import java.util.ArrayList;

public class dot_Graph  {

    private boolean strict;
    private String name;
    private String type;





    private dot_GraphvizModel dot_graphvizmodel;


    public dot_Graph(
        boolean strict,        String name,        String type    ) {
        this.strict = strict;
        this.name = name;
        this.type = type;
    }


    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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