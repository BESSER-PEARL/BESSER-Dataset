





import java.util.List;
import java.util.ArrayList;

public class MyClass2  {

    private String attribute3;
    private String attribute2;
    private int attribute;



    public MyClass2(
        String attribute3,        String attribute2,        int attribute    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute = attribute;
    }


    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
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