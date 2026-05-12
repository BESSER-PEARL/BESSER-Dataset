





import java.util.List;
import java.util.ArrayList;

public class MyClass  {

    private String attribute3;
    private String attribute2;
    private String attribute;
    private String attribute4;



    public MyClass(
        String attribute3,        String attribute2,        String attribute,        String attribute4    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.attribute4 = attribute4;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute4() {
        return attribute4;
    }

    public void setAttribute4(String attribute4) {
        this.attribute4 = attribute4;
    }


}