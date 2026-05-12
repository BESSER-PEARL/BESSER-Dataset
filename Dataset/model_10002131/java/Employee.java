





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String attribute3;
    private String attribute2;
    private String attribute;
    private String attribute31;



    public Employee(
        String attribute3,        String attribute2,        String attribute,        String attribute31    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.attribute31 = attribute31;
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
    public String getAttribute31() {
        return attribute31;
    }

    public void setAttribute31(String attribute31) {
        this.attribute31 = attribute31;
    }


}