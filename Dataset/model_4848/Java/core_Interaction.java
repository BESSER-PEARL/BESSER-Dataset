





import java.util.List;
import java.util.ArrayList;

public class core_Interaction extends IdentifiedElement {

    private String direction;





    private core_Actor core_actor;


    public core_Interaction(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public core_Actor getCore_actor() {
        return core_actor;
    }

    public void setCore_actor(core_Actor core_actor) {
        this.core_actor = core_actor;
    }

}