





import java.util.List;
import java.util.ArrayList;

public class TreeMapViewer_TreeMapContainer extends TreeMapItem {






    private List<TreeMapViewer_TreeMapItem> treemapviewer_treemapitems;


    public TreeMapViewer_TreeMapContainer(
    ) {
        super(
        );
        this.treemapviewer_treemapitems = new ArrayList<>();
    }

    public TreeMapViewer_TreeMapContainer(
        ArrayList<TreeMapViewer_TreeMapItem> treemapviewer_treemapitems    ) {
        this.treemapviewer_treemapitems = treemapviewer_treemapitems;
    }


    public List<TreeMapViewer_TreeMapItem> getTreemapviewer_treemapitems() {
        return treemapviewer_treemapitems;
    }

    public void addTreemapviewer_treemapitem(Treemapviewer_treemapitem treemapviewer_treemapitem) {
        this.treemapviewer_treemapitems.add(treemapviewer_treemapitem);
    }

}