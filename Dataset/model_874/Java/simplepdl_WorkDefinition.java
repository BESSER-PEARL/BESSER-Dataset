





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition extends ProcessElement {

    private int max_time;
    private int min_time;
    private String name;



    public simplepdl_WorkDefinition(
        int max_time,        int min_time,        String name    ) {
        super(
        );
        this.max_time = max_time;
        this.min_time = min_time;
        this.name = name;
    }


    public int getMax_time() {
        return max_time;
    }

    public void setMax_time(int max_time) {
        this.max_time = max_time;
    }
    public int getMin_time() {
        return min_time;
    }

    public void setMin_time(int min_time) {
        this.min_time = min_time;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}