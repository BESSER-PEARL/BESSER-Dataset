





import java.util.List;
import java.util.ArrayList;

public class lobj_ThemeNode extends Node {






    private lobj_Theme lobj_theme;




    private List<lobj_Node> lobj_nodes;


    public lobj_ThemeNode(
    ) {
        super(
        );
        this.lobj_nodes = new ArrayList<>();
    }

    public lobj_ThemeNode(
        ArrayList<lobj_Node> lobj_nodes    ) {
        this.lobj_nodes = lobj_nodes;
    }


    public lobj_Theme getLobj_theme() {
        return lobj_theme;
    }

    public void setLobj_theme(lobj_Theme lobj_theme) {
        this.lobj_theme = lobj_theme;
    }
    public List<lobj_Node> getLobj_nodes() {
        return lobj_nodes;
    }

    public void addLobj_node(Lobj_node lobj_node) {
        this.lobj_nodes.add(lobj_node);
    }

}