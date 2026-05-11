





import java.util.List;
import java.util.ArrayList;

public class UATMM_structure_AttackTree  {






    private List<UATMM_structure_Edge> uatmm_structure_edges;




    private List<UATMM_structure_TreeMetaData> uatmm_structure_treemetadatas;


    public UATMM_structure_AttackTree(
    ) {
        this.uatmm_structure_edges = new ArrayList<>();
        this.uatmm_structure_treemetadatas = new ArrayList<>();
    }

    public UATMM_structure_AttackTree(
        ArrayList<UATMM_structure_Edge> uatmm_structure_edges,        ArrayList<UATMM_structure_TreeMetaData> uatmm_structure_treemetadatas    ) {
        this.uatmm_structure_edges = uatmm_structure_edges;
        this.uatmm_structure_treemetadatas = uatmm_structure_treemetadatas;
    }


    public List<UATMM_structure_Edge> getUatmm_structure_edges() {
        return uatmm_structure_edges;
    }

    public void addUatmm_structure_edge(Uatmm_structure_edge uatmm_structure_edge) {
        this.uatmm_structure_edges.add(uatmm_structure_edge);
    }
    public List<UATMM_structure_TreeMetaData> getUatmm_structure_treemetadatas() {
        return uatmm_structure_treemetadatas;
    }

    public void addUatmm_structure_treemetadata(Uatmm_structure_treemetadata uatmm_structure_treemetadata) {
        this.uatmm_structure_treemetadatas.add(uatmm_structure_treemetadata);
    }

}