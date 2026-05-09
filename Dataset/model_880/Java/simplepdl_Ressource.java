





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private String name;
    private int count;



    public simplepdl_Ressource(
        String name,        int count    ) {
        super(
        );
        this.name = name;
        this.count = count;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }


}