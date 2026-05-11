





import java.util.List;
import java.util.ArrayList;

public class fmp_Node  {

    private int min;
    private String id;
    private int max;





    private List<fmp_Node> fmp_nodes;




    private List<fmp_Node> fmp_nodes;




    private fmp_Node fmp_node;




    private fmp_Feature fmp_feature;




    private fmp_Feature fmp_feature;


    public fmp_Node(
        int min,        String id,        int max    ) {
        this.min = min;
        this.id = id;
        this.max = max;
        this.fmp_nodes = new ArrayList<>();
        this.fmp_nodes = new ArrayList<>();
    }

    public fmp_Node(
        int min,        String id,        int max        ArrayList<fmp_Node> fmp_nodes,        ArrayList<fmp_Node> fmp_nodes    ) {
        this.min = min;
        this.id = id;
        this.max = max;
        this.fmp_nodes = fmp_nodes;
        this.fmp_nodes = fmp_nodes;
    }

    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public List<fmp_Node> getFmp_nodes() {
        return fmp_nodes;
    }

    public void addFmp_node(Fmp_node fmp_node) {
        this.fmp_nodes.add(fmp_node);
    }
    public List<fmp_Node> getFmp_nodes() {
        return fmp_nodes;
    }

    public void addFmp_node(Fmp_node fmp_node) {
        this.fmp_nodes.add(fmp_node);
    }
    public fmp_Node getFmp_node() {
        return fmp_node;
    }

    public void setFmp_node(fmp_Node fmp_node) {
        this.fmp_node = fmp_node;
    }
    public fmp_Feature getFmp_feature() {
        return fmp_feature;
    }

    public void setFmp_feature(fmp_Feature fmp_feature) {
        this.fmp_feature = fmp_feature;
    }
    public fmp_Feature getFmp_feature() {
        return fmp_feature;
    }

    public void setFmp_feature(fmp_Feature fmp_feature) {
        this.fmp_feature = fmp_feature;
    }

}