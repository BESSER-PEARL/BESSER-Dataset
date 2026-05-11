





import java.util.List;
import java.util.ArrayList;

public class xDrone_GoTo extends Command {

    private String object_name;



    public xDrone_GoTo(
        String object_name    ) {
        super(
        );
        this.object_name = object_name;
    }


    public String getObject_name() {
        return object_name;
    }

    public void setObject_name(String object_name) {
        this.object_name = object_name;
    }


}