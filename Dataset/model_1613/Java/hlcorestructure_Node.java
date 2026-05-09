





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_Node extends PnObject {






    private hlcorestructure_Arc hlcorestructure_arc;




    private List<hlcorestructure_Arc> hlcorestructure_arcs;




    private hlcorestructure_Arc hlcorestructure_arc;




    private List<hlcorestructure_Arc> hlcorestructure_arcs;


    public hlcorestructure_Node(
    ) {
        super(
        );
        this.hlcorestructure_arcs = new ArrayList<>();
        this.hlcorestructure_arcs = new ArrayList<>();
    }

    public hlcorestructure_Node(
        ArrayList<hlcorestructure_Arc> hlcorestructure_arcs,        ArrayList<hlcorestructure_Arc> hlcorestructure_arcs    ) {
        this.hlcorestructure_arcs = hlcorestructure_arcs;
        this.hlcorestructure_arcs = hlcorestructure_arcs;
    }


    public hlcorestructure_Arc getHlcorestructure_arc() {
        return hlcorestructure_arc;
    }

    public void setHlcorestructure_arc(hlcorestructure_Arc hlcorestructure_arc) {
        this.hlcorestructure_arc = hlcorestructure_arc;
    }
    public List<hlcorestructure_Arc> getHlcorestructure_arcs() {
        return hlcorestructure_arcs;
    }

    public void addHlcorestructure_arc(Hlcorestructure_arc hlcorestructure_arc) {
        this.hlcorestructure_arcs.add(hlcorestructure_arc);
    }
    public hlcorestructure_Arc getHlcorestructure_arc() {
        return hlcorestructure_arc;
    }

    public void setHlcorestructure_arc(hlcorestructure_Arc hlcorestructure_arc) {
        this.hlcorestructure_arc = hlcorestructure_arc;
    }
    public List<hlcorestructure_Arc> getHlcorestructure_arcs() {
        return hlcorestructure_arcs;
    }

    public void addHlcorestructure_arc(Hlcorestructure_arc hlcorestructure_arc) {
        this.hlcorestructure_arcs.add(hlcorestructure_arc);
    }

}