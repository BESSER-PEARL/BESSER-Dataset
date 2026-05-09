





import java.util.List;
import java.util.ArrayList;

public class pycom_Sensor  {






    private pycom_BoardMember pycom_boardmember;




    private pycom_ModuleType pycom_moduletype;


    public pycom_Sensor(
    ) {
    }



    public pycom_BoardMember getPycom_boardmember() {
        return pycom_boardmember;
    }

    public void setPycom_boardmember(pycom_BoardMember pycom_boardmember) {
        this.pycom_boardmember = pycom_boardmember;
    }
    public pycom_ModuleType getPycom_moduletype() {
        return pycom_moduletype;
    }

    public void setPycom_moduletype(pycom_ModuleType pycom_moduletype) {
        this.pycom_moduletype = pycom_moduletype;
    }

}