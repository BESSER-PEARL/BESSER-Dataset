





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition extends Node {

    private String id;



    public petrinet_Transition(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}