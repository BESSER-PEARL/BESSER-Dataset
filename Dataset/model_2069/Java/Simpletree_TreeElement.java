





import java.util.List;
import java.util.ArrayList;

public class Simpletree_TreeElement  {

    private int index;
    private String name;





    private Simpletree_File simpletree_file;


    public Simpletree_TreeElement(
        int index,        String name    ) {
        this.index = index;
        this.name = name;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Simpletree_File getSimpletree_file() {
        return simpletree_file;
    }

    public void setSimpletree_file(Simpletree_File simpletree_file) {
        this.simpletree_file = simpletree_file;
    }

}