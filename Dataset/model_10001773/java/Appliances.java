





import java.util.List;
import java.util.ArrayList;

public class Appliances  {

    private boolean On_status;
    private boolean Off_status;



    public Appliances(
        boolean On_status,        boolean Off_status    ) {
        this.On_status = On_status;
        this.Off_status = Off_status;
    }


    public boolean getOn_status() {
        return On_status;
    }

    public void setOn_status(boolean On_status) {
        this.On_status = On_status;
    }
    public boolean getOff_status() {
        return Off_status;
    }

    public void setOff_status(boolean Off_status) {
        this.Off_status = Off_status;
    }


}