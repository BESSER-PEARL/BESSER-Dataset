





import java.util.List;
import java.util.ArrayList;

public class graphbt_LayoutList  {






    private List<graphbt_Layout> graphbt_layouts;


    public graphbt_LayoutList(
    ) {
        this.graphbt_layouts = new ArrayList<>();
    }

    public graphbt_LayoutList(
        ArrayList<graphbt_Layout> graphbt_layouts    ) {
        this.graphbt_layouts = graphbt_layouts;
    }


    public List<graphbt_Layout> getGraphbt_layouts() {
        return graphbt_layouts;
    }

    public void addGraphbt_layout(Graphbt_layout graphbt_layout) {
        this.graphbt_layouts.add(graphbt_layout);
    }

}