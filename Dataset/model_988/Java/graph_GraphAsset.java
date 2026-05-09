





import java.util.List;
import java.util.ArrayList;

public class graph_GraphAsset extends Identifiable {

    private boolean Encrypted;
    private int Label;





    private graph_NodeResponsibility graph_noderesponsibility;




    private graph_NodeResponsibility graph_noderesponsibility;




    private graph_Edge graph_edge;




    private graph_Subgraphs graph_subgraphs;


    public graph_GraphAsset(
        boolean Encrypted,        int Label    ) {
        super(
        );
        this.Encrypted = Encrypted;
        this.Label = Label;
    }


    public boolean getEncrypted() {
        return Encrypted;
    }

    public void setEncrypted(boolean Encrypted) {
        this.Encrypted = Encrypted;
    }
    public int getLabel() {
        return Label;
    }

    public void setLabel(int Label) {
        this.Label = Label;
    }

    public graph_NodeResponsibility getGraph_noderesponsibility() {
        return graph_noderesponsibility;
    }

    public void setGraph_noderesponsibility(graph_NodeResponsibility graph_noderesponsibility) {
        this.graph_noderesponsibility = graph_noderesponsibility;
    }
    public graph_NodeResponsibility getGraph_noderesponsibility() {
        return graph_noderesponsibility;
    }

    public void setGraph_noderesponsibility(graph_NodeResponsibility graph_noderesponsibility) {
        this.graph_noderesponsibility = graph_noderesponsibility;
    }
    public graph_Edge getGraph_edge() {
        return graph_edge;
    }

    public void setGraph_edge(graph_Edge graph_edge) {
        this.graph_edge = graph_edge;
    }
    public graph_Subgraphs getGraph_subgraphs() {
        return graph_subgraphs;
    }

    public void setGraph_subgraphs(graph_Subgraphs graph_subgraphs) {
        this.graph_subgraphs = graph_subgraphs;
    }

}