





import java.util.List;
import java.util.ArrayList;

public class myffbd_PortType  {

    private String type;





    private myffbd_Function myffbd_function;


    public myffbd_PortType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public myffbd_Function getMyffbd_function() {
        return myffbd_function;
    }

    public void setMyffbd_function(myffbd_Function myffbd_function) {
        this.myffbd_function = myffbd_function;
    }

}