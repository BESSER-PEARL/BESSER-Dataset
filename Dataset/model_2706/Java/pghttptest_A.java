





import java.util.List;
import java.util.ArrayList;

public class pghttptest_A  {

    private String name;
    private int value;





    private pghttptest_Root pghttptest_root;


    public pghttptest_A(
        String name,        int value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public pghttptest_Root getPghttptest_root() {
        return pghttptest_root;
    }

    public void setPghttptest_root(pghttptest_Root pghttptest_root) {
        this.pghttptest_root = pghttptest_root;
    }

}