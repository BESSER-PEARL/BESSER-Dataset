





import java.util.List;
import java.util.ArrayList;

public class ioT_PyList extends VarOrList {






    private ioT_AddToList iot_addtolist;




    private ioT_ClearListAction iot_clearlistaction;


    public ioT_PyList(
    ) {
        super(
        );
    }



    public ioT_AddToList getIot_addtolist() {
        return iot_addtolist;
    }

    public void setIot_addtolist(ioT_AddToList iot_addtolist) {
        this.iot_addtolist = iot_addtolist;
    }
    public ioT_ClearListAction getIot_clearlistaction() {
        return iot_clearlistaction;
    }

    public void setIot_clearlistaction(ioT_ClearListAction iot_clearlistaction) {
        this.iot_clearlistaction = iot_clearlistaction;
    }

}