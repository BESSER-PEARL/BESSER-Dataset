





import java.util.List;
import java.util.ArrayList;

public class egt_GraphModel  {






    private List<egt_Vertex> egt_vertexs;




    private egt_ColorRegistry egt_colorregistry;


    public egt_GraphModel(
    ) {
        this.egt_vertexs = new ArrayList<>();
    }

    public egt_GraphModel(
        ArrayList<egt_Vertex> egt_vertexs    ) {
        this.egt_vertexs = egt_vertexs;
    }


    public List<egt_Vertex> getEgt_vertexs() {
        return egt_vertexs;
    }

    public void addEgt_vertex(Egt_vertex egt_vertex) {
        this.egt_vertexs.add(egt_vertex);
    }
    public egt_ColorRegistry getEgt_colorregistry() {
        return egt_colorregistry;
    }

    public void setEgt_colorregistry(egt_ColorRegistry egt_colorregistry) {
        this.egt_colorregistry = egt_colorregistry;
    }

}