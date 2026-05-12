





import java.util.List;
import java.util.ArrayList;

public class Data_entry  {

    private String attribute2;
    private String attribute;



    public Data_entry(
        String attribute2,        String attribute    ) {
        this.attribute2 = attribute2;
        this.attribute = attribute;
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


}