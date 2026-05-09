





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition extends ProcessElement {

    private int max_time;
    private String name;
    private int min_time;





    private simplepdl_RessourceLink simplepdl_ressourcelink;


    public simplepdl_WorkDefinition(
        int max_time,        String name,        int min_time    ) {
        super(
        );
        this.max_time = max_time;
        this.name = name;
        this.min_time = min_time;
    }


    public int getMax_time() {
        return max_time;
    }

    public void setMax_time(int max_time) {
        this.max_time = max_time;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMin_time() {
        return min_time;
    }

    public void setMin_time(int min_time) {
        this.min_time = min_time;
    }

    public simplepdl_RessourceLink getSimplepdl_ressourcelink() {
        return simplepdl_ressourcelink;
    }

    public void setSimplepdl_ressourcelink(simplepdl_RessourceLink simplepdl_ressourcelink) {
        this.simplepdl_ressourcelink = simplepdl_ressourcelink;
    }

}