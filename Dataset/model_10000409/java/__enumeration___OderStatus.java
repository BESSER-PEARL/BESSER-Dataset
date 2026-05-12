





import java.util.List;
import java.util.ArrayList;

public class __enumeration___OderStatus  {

    private String return;
    private String hold;
    private String new;
    private String delivery;
    private String closed;
    private String shipped;



    public __enumeration___OderStatus(
        String return,        String hold,        String new,        String delivery,        String closed,        String shipped    ) {
        this.return = return;
        this.hold = hold;
        this.new = new;
        this.delivery = delivery;
        this.closed = closed;
        this.shipped = shipped;
    }


    public String getReturn() {
        return return;
    }

    public void setReturn(String return) {
        this.return = return;
    }
    public String getHold() {
        return hold;
    }

    public void setHold(String hold) {
        this.hold = hold;
    }
    public String getNew() {
        return new;
    }

    public void setNew(String new) {
        this.new = new;
    }
    public String getDelivery() {
        return delivery;
    }

    public void setDelivery(String delivery) {
        this.delivery = delivery;
    }
    public String getClosed() {
        return closed;
    }

    public void setClosed(String closed) {
        this.closed = closed;
    }
    public String getShipped() {
        return shipped;
    }

    public void setShipped(String shipped) {
        this.shipped = shipped;
    }


}