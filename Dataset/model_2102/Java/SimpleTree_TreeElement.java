





import java.util.List;
import java.util.ArrayList;

public class SimpleTree_TreeElement  {

    private String name;
    private int index;





    private SimpleTree_File simpletree_file;


    public SimpleTree_TreeElement(
        String name,        int index    ) {
        this.name = name;
        this.index = index;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public SimpleTree_File getSimpletree_file() {
        return simpletree_file;
    }

    public void setSimpletree_file(SimpleTree_File simpletree_file) {
        this.simpletree_file = simpletree_file;
    }

}