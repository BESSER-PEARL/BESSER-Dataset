





import java.util.List;
import java.util.ArrayList;

public class vml_Node  {

    private String title;





    private vml_Graph vml_graph;


    public vml_Node(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public vml_Graph getVml_graph() {
        return vml_graph;
    }

    public void setVml_graph(vml_Graph vml_graph) {
        this.vml_graph = vml_graph;
    }

}