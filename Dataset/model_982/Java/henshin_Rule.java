





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends TransformationUnit {






    private henshin_TransformationSystem henshin_transformationsystem;




    private henshin_TransformationSystem henshin_transformationsystem;




    private henshin_Graph henshin_graph;




    private henshin_AttributeCondition henshin_attributecondition;




    private List<henshin_AttributeCondition> henshin_attributeconditions;




    private henshin_Graph henshin_graph;


    public henshin_Rule(
    ) {
        super(
        );
        this.henshin_attributeconditions = new ArrayList<>();
    }

    public henshin_Rule(
        ArrayList<henshin_AttributeCondition> henshin_attributeconditions    ) {
        this.henshin_attributeconditions = henshin_attributeconditions;
    }


    public henshin_TransformationSystem getHenshin_transformationsystem() {
        return henshin_transformationsystem;
    }

    public void setHenshin_transformationsystem(henshin_TransformationSystem henshin_transformationsystem) {
        this.henshin_transformationsystem = henshin_transformationsystem;
    }
    public henshin_TransformationSystem getHenshin_transformationsystem() {
        return henshin_transformationsystem;
    }

    public void setHenshin_transformationsystem(henshin_TransformationSystem henshin_transformationsystem) {
        this.henshin_transformationsystem = henshin_transformationsystem;
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }
    public henshin_AttributeCondition getHenshin_attributecondition() {
        return henshin_attributecondition;
    }

    public void setHenshin_attributecondition(henshin_AttributeCondition henshin_attributecondition) {
        this.henshin_attributecondition = henshin_attributecondition;
    }
    public List<henshin_AttributeCondition> getHenshin_attributeconditions() {
        return henshin_attributeconditions;
    }

    public void addHenshin_attributecondition(Henshin_attributecondition henshin_attributecondition) {
        this.henshin_attributeconditions.add(henshin_attributecondition);
    }
    public henshin_Graph getHenshin_graph() {
        return henshin_graph;
    }

    public void setHenshin_graph(henshin_Graph henshin_graph) {
        this.henshin_graph = henshin_graph;
    }

}