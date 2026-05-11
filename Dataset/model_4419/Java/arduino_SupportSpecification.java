





import java.util.List;
import java.util.ArrayList;

public class arduino_SupportSpecification  {

    private String supportType;





    private arduino_InAcquireOperation arduino_inacquireoperation;


    public arduino_SupportSpecification(
        String supportType    ) {
        this.supportType = supportType;
    }


    public String getSupporttype() {
        return supportType;
    }

    public void setSupporttype(String supportType) {
        this.supportType = supportType;
    }

    public arduino_InAcquireOperation getArduino_inacquireoperation() {
        return arduino_inacquireoperation;
    }

    public void setArduino_inacquireoperation(arduino_InAcquireOperation arduino_inacquireoperation) {
        this.arduino_inacquireoperation = arduino_inacquireoperation;
    }

}