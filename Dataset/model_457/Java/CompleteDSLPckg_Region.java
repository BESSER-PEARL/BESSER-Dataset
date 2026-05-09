





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Region extends Namespace, RedefinableElement {






    private CompleteDSLPckg_State completedslpckg_state;




    private CompleteDSLPckg_Vertex completedslpckg_vertex;




    private List<CompleteDSLPckg_Vertex> completedslpckg_vertexs;




    private CompleteDSLPckg_Region completedslpckg_region;




    private CompleteDSLPckg_State completedslpckg_state;


    public CompleteDSLPckg_Region(
    ) {
        super(
        );
        this.completedslpckg_vertexs = new ArrayList<>();
    }

    public CompleteDSLPckg_Region(
        ArrayList<CompleteDSLPckg_Vertex> completedslpckg_vertexs    ) {
        this.completedslpckg_vertexs = completedslpckg_vertexs;
    }


    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }
    public CompleteDSLPckg_Vertex getCompletedslpckg_vertex() {
        return completedslpckg_vertex;
    }

    public void setCompletedslpckg_vertex(CompleteDSLPckg_Vertex completedslpckg_vertex) {
        this.completedslpckg_vertex = completedslpckg_vertex;
    }
    public List<CompleteDSLPckg_Vertex> getCompletedslpckg_vertexs() {
        return completedslpckg_vertexs;
    }

    public void addCompletedslpckg_vertex(Completedslpckg_vertex completedslpckg_vertex) {
        this.completedslpckg_vertexs.add(completedslpckg_vertex);
    }
    public CompleteDSLPckg_Region getCompletedslpckg_region() {
        return completedslpckg_region;
    }

    public void setCompletedslpckg_region(CompleteDSLPckg_Region completedslpckg_region) {
        this.completedslpckg_region = completedslpckg_region;
    }
    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }

}