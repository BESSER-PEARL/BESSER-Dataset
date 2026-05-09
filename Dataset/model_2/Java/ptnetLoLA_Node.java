





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Node  {

    private String name;
    private String type;





    private ptnetLoLA_Arc ptnetlola_arc;




    private List<ptnetLoLA_Arc> ptnetlola_arcs;




    private ptnetLoLA_Annotation ptnetlola_annotation;




    private List<ptnetLoLA_Arc> ptnetlola_arcs;




    private ptnetLoLA_Arc ptnetlola_arc;


    public ptnetLoLA_Node(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.ptnetlola_arcs = new ArrayList<>();
        this.ptnetlola_arcs = new ArrayList<>();
    }

    public ptnetLoLA_Node(
        String name,        String type        ArrayList<ptnetLoLA_Arc> ptnetlola_arcs,        ArrayList<ptnetLoLA_Arc> ptnetlola_arcs    ) {
        this.name = name;
        this.type = type;
        this.ptnetlola_arcs = ptnetlola_arcs;
        this.ptnetlola_arcs = ptnetlola_arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ptnetLoLA_Arc getPtnetlola_arc() {
        return ptnetlola_arc;
    }

    public void setPtnetlola_arc(ptnetLoLA_Arc ptnetlola_arc) {
        this.ptnetlola_arc = ptnetlola_arc;
    }
    public List<ptnetLoLA_Arc> getPtnetlola_arcs() {
        return ptnetlola_arcs;
    }

    public void addPtnetlola_arc(Ptnetlola_arc ptnetlola_arc) {
        this.ptnetlola_arcs.add(ptnetlola_arc);
    }
    public ptnetLoLA_Annotation getPtnetlola_annotation() {
        return ptnetlola_annotation;
    }

    public void setPtnetlola_annotation(ptnetLoLA_Annotation ptnetlola_annotation) {
        this.ptnetlola_annotation = ptnetlola_annotation;
    }
    public List<ptnetLoLA_Arc> getPtnetlola_arcs() {
        return ptnetlola_arcs;
    }

    public void addPtnetlola_arc(Ptnetlola_arc ptnetlola_arc) {
        this.ptnetlola_arcs.add(ptnetlola_arc);
    }
    public ptnetLoLA_Arc getPtnetlola_arc() {
        return ptnetlola_arc;
    }

    public void setPtnetlola_arc(ptnetLoLA_Arc ptnetlola_arc) {
        this.ptnetlola_arc = ptnetlola_arc;
    }

}