





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Edge_Declaration extends Input_Declaration {

    private String edge;



    public iec61131_interfaces_Edge_Declaration(
        String edge    ) {
        super(
        );
        this.edge = edge;
    }


    public String getEdge() {
        return edge;
    }

    public void setEdge(String edge) {
        this.edge = edge;
    }


}