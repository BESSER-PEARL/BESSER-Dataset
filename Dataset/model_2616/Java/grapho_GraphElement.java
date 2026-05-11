





import java.util.List;
import java.util.ArrayList;

public class grapho_GraphElement  {

    private String name;





    private grapho_GraphO grapho_grapho;


    public grapho_GraphElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public grapho_GraphO getGrapho_grapho() {
        return grapho_grapho;
    }

    public void setGrapho_grapho(grapho_GraphO grapho_grapho) {
        this.grapho_grapho = grapho_grapho;
    }

}