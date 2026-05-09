





import java.util.List;
import java.util.ArrayList;

public class henshin_Node extends NamedElement, GraphElement {






    private henshin_Attribute henshin_attribute;




    private List<henshin_Edge> henshin_edges;




    private List<henshin_Attribute> henshin_attributes;




    private List<henshin_Edge> henshin_edges;




    private henshin_Edge henshin_edge;




    private henshin_Mapping henshin_mapping;




    private henshin_Mapping henshin_mapping;




    private henshin_Edge henshin_edge;


    public henshin_Node(
    ) {
        super(
        );
        this.henshin_edges = new ArrayList<>();
        this.henshin_attributes = new ArrayList<>();
        this.henshin_edges = new ArrayList<>();
    }

    public henshin_Node(
        ArrayList<henshin_Edge> henshin_edges,        ArrayList<henshin_Attribute> henshin_attributes,        ArrayList<henshin_Edge> henshin_edges    ) {
        this.henshin_edges = henshin_edges;
        this.henshin_attributes = henshin_attributes;
        this.henshin_edges = henshin_edges;
    }


    public henshin_Attribute getHenshin_attribute() {
        return henshin_attribute;
    }

    public void setHenshin_attribute(henshin_Attribute henshin_attribute) {
        this.henshin_attribute = henshin_attribute;
    }
    public List<henshin_Edge> getHenshin_edges() {
        return henshin_edges;
    }

    public void addHenshin_edge(Henshin_edge henshin_edge) {
        this.henshin_edges.add(henshin_edge);
    }
    public List<henshin_Attribute> getHenshin_attributes() {
        return henshin_attributes;
    }

    public void addHenshin_attribute(Henshin_attribute henshin_attribute) {
        this.henshin_attributes.add(henshin_attribute);
    }
    public List<henshin_Edge> getHenshin_edges() {
        return henshin_edges;
    }

    public void addHenshin_edge(Henshin_edge henshin_edge) {
        this.henshin_edges.add(henshin_edge);
    }
    public henshin_Edge getHenshin_edge() {
        return henshin_edge;
    }

    public void setHenshin_edge(henshin_Edge henshin_edge) {
        this.henshin_edge = henshin_edge;
    }
    public henshin_Mapping getHenshin_mapping() {
        return henshin_mapping;
    }

    public void setHenshin_mapping(henshin_Mapping henshin_mapping) {
        this.henshin_mapping = henshin_mapping;
    }
    public henshin_Mapping getHenshin_mapping() {
        return henshin_mapping;
    }

    public void setHenshin_mapping(henshin_Mapping henshin_mapping) {
        this.henshin_mapping = henshin_mapping;
    }
    public henshin_Edge getHenshin_edge() {
        return henshin_edge;
    }

    public void setHenshin_edge(henshin_Edge henshin_edge) {
        this.henshin_edge = henshin_edge;
    }

}