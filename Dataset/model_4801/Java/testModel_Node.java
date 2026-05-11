





import java.util.List;
import java.util.ArrayList;

public class testModel_Node  {

    private String bigdeci;
    private String name;
    private boolean bool;
    private String Boolean;
    private String bigint;
    private String byte;





    private List<testModel_Node> testmodel_nodes;




    private List<testModel_ContainedLeaf> testmodel_containedleafs;


    public testModel_Node(
        String bigdeci,        String name,        boolean bool,        String Boolean,        String bigint,        String byte    ) {
        this.bigdeci = bigdeci;
        this.name = name;
        this.bool = bool;
        this.Boolean = Boolean;
        this.bigint = bigint;
        this.byte = byte;
        this.testmodel_nodes = new ArrayList<>();
        this.testmodel_containedleafs = new ArrayList<>();
    }

    public testModel_Node(
        String bigdeci,        String name,        boolean bool,        String Boolean,        String bigint,        String byte        ArrayList<testModel_Node> testmodel_nodes,        ArrayList<testModel_ContainedLeaf> testmodel_containedleafs    ) {
        this.bigdeci = bigdeci;
        this.name = name;
        this.bool = bool;
        this.Boolean = Boolean;
        this.bigint = bigint;
        this.byte = byte;
        this.testmodel_nodes = testmodel_nodes;
        this.testmodel_containedleafs = testmodel_containedleafs;
    }

    public String getBigdeci() {
        return bigdeci;
    }

    public void setBigdeci(String bigdeci) {
        this.bigdeci = bigdeci;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getBool() {
        return bool;
    }

    public void setBool(boolean bool) {
        this.bool = bool;
    }
    public String getBoolean() {
        return Boolean;
    }

    public void setBoolean(String Boolean) {
        this.Boolean = Boolean;
    }
    public String getBigint() {
        return bigint;
    }

    public void setBigint(String bigint) {
        this.bigint = bigint;
    }
    public String getByte() {
        return byte;
    }

    public void setByte(String byte) {
        this.byte = byte;
    }

    public List<testModel_Node> getTestmodel_nodes() {
        return testmodel_nodes;
    }

    public void addTestmodel_node(Testmodel_node testmodel_node) {
        this.testmodel_nodes.add(testmodel_node);
    }
    public List<testModel_ContainedLeaf> getTestmodel_containedleafs() {
        return testmodel_containedleafs;
    }

    public void addTestmodel_containedleaf(Testmodel_containedleaf testmodel_containedleaf) {
        this.testmodel_containedleafs.add(testmodel_containedleaf);
    }

}