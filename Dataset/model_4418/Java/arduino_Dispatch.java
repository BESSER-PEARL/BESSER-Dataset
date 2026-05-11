





import java.util.List;
import java.util.ArrayList;

public class arduino_Dispatch extends OutOnlyMessage {

    private String name;



    public arduino_Dispatch(
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