





import java.util.List;
import java.util.ArrayList;

public class fsm_InitialState extends SuperState {

    private String name;



    public fsm_InitialState(
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