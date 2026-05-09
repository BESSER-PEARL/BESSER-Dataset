





import java.util.List;
import java.util.ArrayList;

public class pycom_Pin  {






    private pycom_Sensor pycom_sensor;




    private pycom_Function pycom_function;


    public pycom_Pin(
    ) {
    }



    public pycom_Sensor getPycom_sensor() {
        return pycom_sensor;
    }

    public void setPycom_sensor(pycom_Sensor pycom_sensor) {
        this.pycom_sensor = pycom_sensor;
    }
    public pycom_Function getPycom_function() {
        return pycom_function;
    }

    public void setPycom_function(pycom_Function pycom_function) {
        this.pycom_function = pycom_function;
    }

}