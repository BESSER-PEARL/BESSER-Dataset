





import java.util.List;
import java.util.ArrayList;

public class pycom_Actuator extends BoardMember {






    private pycom_ModuleType pycom_moduletype;




    private pycom_ModuleName pycom_modulename;




    private pycom_Pin pycom_pin;


    public pycom_Actuator(
    ) {
        super(
        );
    }



    public pycom_ModuleType getPycom_moduletype() {
        return pycom_moduletype;
    }

    public void setPycom_moduletype(pycom_ModuleType pycom_moduletype) {
        this.pycom_moduletype = pycom_moduletype;
    }
    public pycom_ModuleName getPycom_modulename() {
        return pycom_modulename;
    }

    public void setPycom_modulename(pycom_ModuleName pycom_modulename) {
        this.pycom_modulename = pycom_modulename;
    }
    public pycom_Pin getPycom_pin() {
        return pycom_pin;
    }

    public void setPycom_pin(pycom_Pin pycom_pin) {
        this.pycom_pin = pycom_pin;
    }

}