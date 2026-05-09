





import java.util.List;
import java.util.ArrayList;

public class graph_GLayouting  {

    private String layout;





    private graph_GLayoutOptions graph_glayoutoptions;


    public graph_GLayouting(
        String layout    ) {
        this.layout = layout;
    }


    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }

    public graph_GLayoutOptions getGraph_glayoutoptions() {
        return graph_glayoutoptions;
    }

    public void setGraph_glayoutoptions(graph_GLayoutOptions graph_glayoutoptions) {
        this.graph_glayoutoptions = graph_glayoutoptions;
    }

}