





import java.util.List;
import java.util.ArrayList;

public class graph_GLayouting  {

    private String layout;





    private List<graph_StringToObjectMapEntry> graph_stringtoobjectmapentrys;


    public graph_GLayouting(
        String layout    ) {
        this.layout = layout;
        this.graph_stringtoobjectmapentrys = new ArrayList<>();
    }

    public graph_GLayouting(
        String layout        ArrayList<graph_StringToObjectMapEntry> graph_stringtoobjectmapentrys    ) {
        this.layout = layout;
        this.graph_stringtoobjectmapentrys = graph_stringtoobjectmapentrys;
    }

    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }

    public List<graph_StringToObjectMapEntry> getGraph_stringtoobjectmapentrys() {
        return graph_stringtoobjectmapentrys;
    }

    public void addGraph_stringtoobjectmapentry(Graph_stringtoobjectmapentry graph_stringtoobjectmapentry) {
        this.graph_stringtoobjectmapentrys.add(graph_stringtoobjectmapentry);
    }

}