





import java.util.List;
import java.util.ArrayList;

public class arduino_Request extends OutInMessage {






    private arduino_DemandRequest arduino_demandrequest;


    public arduino_Request(
    ) {
        super(
        );
    }



    public arduino_DemandRequest getArduino_demandrequest() {
        return arduino_demandrequest;
    }

    public void setArduino_demandrequest(arduino_DemandRequest arduino_demandrequest) {
        this.arduino_demandrequest = arduino_demandrequest;
    }

}