





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private int count;
    private String name;



    public simplepdl_Ressource(
        int count,        String name    ) {
        super(
        );
        this.count = count;
        this.name = name;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}