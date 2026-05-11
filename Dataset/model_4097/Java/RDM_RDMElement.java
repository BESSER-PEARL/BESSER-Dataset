





import java.util.List;
import java.util.ArrayList;

public class RDM_RDMElement  {

    private String name;
    private int length;



    public RDM_RDMElement(
        String name,        int length    ) {
        this.name = name;
        this.length = length;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}