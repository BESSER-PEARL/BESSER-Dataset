





import java.util.List;
import java.util.ArrayList;

public class ABC_Element  {

    private int id;





    private ABC_Root abc_root;




    private ABC_Element abc_element;


    public ABC_Element(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ABC_Root getAbc_root() {
        return abc_root;
    }

    public void setAbc_root(ABC_Root abc_root) {
        this.abc_root = abc_root;
    }
    public ABC_Element getAbc_element() {
        return abc_element;
    }

    public void setAbc_element(ABC_Element abc_element) {
        this.abc_element = abc_element;
    }

}