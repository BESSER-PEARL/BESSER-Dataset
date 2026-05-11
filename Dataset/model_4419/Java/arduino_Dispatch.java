





import java.util.List;
import java.util.ArrayList;

public class arduino_Dispatch extends OutOnlyMessage {

    private String name;





    private arduino_ForwardDispatch arduino_forwarddispatch;


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

    public arduino_ForwardDispatch getArduino_forwarddispatch() {
        return arduino_forwarddispatch;
    }

    public void setArduino_forwarddispatch(arduino_ForwardDispatch arduino_forwarddispatch) {
        this.arduino_forwarddispatch = arduino_forwarddispatch;
    }

}