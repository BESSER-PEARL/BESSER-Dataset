





import java.util.List;
import java.util.ArrayList;

public class Package_Shifts  {

    private String attribute;
    private String attribute2;



    public Package_Shifts(
        String attribute,        String attribute2    ) {
        this.attribute = attribute;
        this.attribute2 = attribute2;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }


}