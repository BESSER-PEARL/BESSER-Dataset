





import java.util.List;
import java.util.ArrayList;

public class UATMM_structure_Node  {

    private String label;
    private String id;
    private String nature;
    private String role;





    private UATMM_structure_Node uatmm_structure_node;




    private UATMM_structure_Edge uatmm_structure_edge;




    private UATMM_structure_AttackTree uatmm_structure_attacktree;




    private UATMM_structure_Edge uatmm_structure_edge;




    private UATMM_structure_Node uatmm_structure_node;




    private UATMM_structure_AttackTree uatmm_structure_attacktree;


    public UATMM_structure_Node(
        String label,        String id,        String nature,        String role    ) {
        this.label = label;
        this.id = id;
        this.nature = nature;
        this.role = role;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public UATMM_structure_Node getUatmm_structure_node() {
        return uatmm_structure_node;
    }

    public void setUatmm_structure_node(UATMM_structure_Node uatmm_structure_node) {
        this.uatmm_structure_node = uatmm_structure_node;
    }
    public UATMM_structure_Edge getUatmm_structure_edge() {
        return uatmm_structure_edge;
    }

    public void setUatmm_structure_edge(UATMM_structure_Edge uatmm_structure_edge) {
        this.uatmm_structure_edge = uatmm_structure_edge;
    }
    public UATMM_structure_AttackTree getUatmm_structure_attacktree() {
        return uatmm_structure_attacktree;
    }

    public void setUatmm_structure_attacktree(UATMM_structure_AttackTree uatmm_structure_attacktree) {
        this.uatmm_structure_attacktree = uatmm_structure_attacktree;
    }
    public UATMM_structure_Edge getUatmm_structure_edge() {
        return uatmm_structure_edge;
    }

    public void setUatmm_structure_edge(UATMM_structure_Edge uatmm_structure_edge) {
        this.uatmm_structure_edge = uatmm_structure_edge;
    }
    public UATMM_structure_Node getUatmm_structure_node() {
        return uatmm_structure_node;
    }

    public void setUatmm_structure_node(UATMM_structure_Node uatmm_structure_node) {
        this.uatmm_structure_node = uatmm_structure_node;
    }
    public UATMM_structure_AttackTree getUatmm_structure_attacktree() {
        return uatmm_structure_attacktree;
    }

    public void setUatmm_structure_attacktree(UATMM_structure_AttackTree uatmm_structure_attacktree) {
        this.uatmm_structure_attacktree = uatmm_structure_attacktree;
    }

}