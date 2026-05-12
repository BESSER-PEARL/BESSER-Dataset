





import java.util.List;
import java.util.ArrayList;

public class Custom_SalesForce_Object  {

    private String Owner;





    private Service_Channel service_channel;


    public Custom_SalesForce_Object(
        String Owner    ) {
        this.Owner = Owner;
    }


    public String getOwner() {
        return Owner;
    }

    public void setOwner(String Owner) {
        this.Owner = Owner;
    }

    public Service_Channel getService_channel() {
        return service_channel;
    }

    public void setService_channel(Service_Channel service_channel) {
        this.service_channel = service_channel;
    }

}