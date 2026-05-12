





import java.util.List;
import java.util.ArrayList;

public class statechart_Event extends IDBase {

    private String name;



    public statechart_Event(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}