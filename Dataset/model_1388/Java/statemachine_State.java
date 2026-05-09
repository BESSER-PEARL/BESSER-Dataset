





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends Vertex {

    private String name;



    public statemachine_State(
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