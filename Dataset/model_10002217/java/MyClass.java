





import java.util.List;
import java.util.ArrayList;

public class MyClass  {

    private String attribute2;
    private int attribute;



    public MyClass(
        String attribute2,        int attribute    ) {
        this.attribute2 = attribute2;
        this.attribute = attribute;
    }


    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public int getAttribute() {
        return attribute;
    }

    public void setAttribute(int attribute) {
        this.attribute = attribute;
    }


}