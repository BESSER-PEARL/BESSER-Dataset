





import java.util.List;
import java.util.ArrayList;

public class ptnet_Node extends PnObject {






    private ptnet_Arc ptnet_arc;




    private ptnet_NodeGraphics ptnet_nodegraphics;




    private List<ptnet_Arc> ptnet_arcs;




    private List<ptnet_Arc> ptnet_arcs;




    private ptnet_NodeGraphics ptnet_nodegraphics;




    private ptnet_Arc ptnet_arc;


    public ptnet_Node(
    ) {
        super(
        );
        this.ptnet_arcs = new ArrayList<>();
        this.ptnet_arcs = new ArrayList<>();
    }

    public ptnet_Node(
        ArrayList<ptnet_Arc> ptnet_arcs,        ArrayList<ptnet_Arc> ptnet_arcs    ) {
        this.ptnet_arcs = ptnet_arcs;
        this.ptnet_arcs = ptnet_arcs;
    }


    public ptnet_Arc getPtnet_arc() {
        return ptnet_arc;
    }

    public void setPtnet_arc(ptnet_Arc ptnet_arc) {
        this.ptnet_arc = ptnet_arc;
    }
    public ptnet_NodeGraphics getPtnet_nodegraphics() {
        return ptnet_nodegraphics;
    }

    public void setPtnet_nodegraphics(ptnet_NodeGraphics ptnet_nodegraphics) {
        this.ptnet_nodegraphics = ptnet_nodegraphics;
    }
    public List<ptnet_Arc> getPtnet_arcs() {
        return ptnet_arcs;
    }

    public void addPtnet_arc(Ptnet_arc ptnet_arc) {
        this.ptnet_arcs.add(ptnet_arc);
    }
    public List<ptnet_Arc> getPtnet_arcs() {
        return ptnet_arcs;
    }

    public void addPtnet_arc(Ptnet_arc ptnet_arc) {
        this.ptnet_arcs.add(ptnet_arc);
    }
    public ptnet_NodeGraphics getPtnet_nodegraphics() {
        return ptnet_nodegraphics;
    }

    public void setPtnet_nodegraphics(ptnet_NodeGraphics ptnet_nodegraphics) {
        this.ptnet_nodegraphics = ptnet_nodegraphics;
    }
    public ptnet_Arc getPtnet_arc() {
        return ptnet_arc;
    }

    public void setPtnet_arc(ptnet_Arc ptnet_arc) {
        this.ptnet_arc = ptnet_arc;
    }

}