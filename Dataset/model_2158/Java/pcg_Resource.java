





import java.util.List;
import java.util.ArrayList;

public class pcg_Resource  {

    private String title;
    private String id;





    private pcg_Vertex pcg_vertex;


    public pcg_Resource(
        String title,        String id    ) {
        this.title = title;
        this.id = id;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public pcg_Vertex getPcg_vertex() {
        return pcg_vertex;
    }

    public void setPcg_vertex(pcg_Vertex pcg_vertex) {
        this.pcg_vertex = pcg_vertex;
    }

}