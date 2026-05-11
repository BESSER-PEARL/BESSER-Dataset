





import java.util.List;
import java.util.ArrayList;

public class DecisionTree_DecisionTrees  {

    private String name;





    private List<DecisionTree_DecisionTreeForEntity> decisiontree_decisiontreeforentitys;


    public DecisionTree_DecisionTrees(
        String name    ) {
        this.name = name;
        this.decisiontree_decisiontreeforentitys = new ArrayList<>();
    }

    public DecisionTree_DecisionTrees(
        String name        ArrayList<DecisionTree_DecisionTreeForEntity> decisiontree_decisiontreeforentitys    ) {
        this.name = name;
        this.decisiontree_decisiontreeforentitys = decisiontree_decisiontreeforentitys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DecisionTree_DecisionTreeForEntity> getDecisiontree_decisiontreeforentitys() {
        return decisiontree_decisiontreeforentitys;
    }

    public void addDecisiontree_decisiontreeforentity(Decisiontree_decisiontreeforentity decisiontree_decisiontreeforentity) {
        this.decisiontree_decisiontreeforentitys.add(decisiontree_decisiontreeforentity);
    }

}