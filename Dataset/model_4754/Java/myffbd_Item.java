





import java.util.List;
import java.util.ArrayList;

public class myffbd_Item  {

    private String name;





    private myffbd_Flow myffbd_flow;


    public myffbd_Item(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myffbd_Flow getMyffbd_flow() {
        return myffbd_flow;
    }

    public void setMyffbd_flow(myffbd_Flow myffbd_flow) {
        this.myffbd_flow = myffbd_flow;
    }

}