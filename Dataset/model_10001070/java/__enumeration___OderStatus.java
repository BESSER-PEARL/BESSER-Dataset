





import java.util.List;
import java.util.ArrayList;

public class __enumeration___OderStatus  {

    private String new;
    private String return;
    private String delivery;
    private String hold;
    private String shipped;
    private String closed;



    public __enumeration___OderStatus(
        String new,        String return,        String delivery,        String hold,        String shipped,        String closed    ) {
        this.new = new;
        this.return = return;
        this.delivery = delivery;
        this.hold = hold;
        this.shipped = shipped;
        this.closed = closed;
    }


    public String getNew() {
        return new;
    }

    public void setNew(String new) {
        this.new = new;
    }
    public String getReturn() {
        return return;
    }

    public void setReturn(String return) {
        this.return = return;
    }
    public String getDelivery() {
        return delivery;
    }

    public void setDelivery(String delivery) {
        this.delivery = delivery;
    }
    public String getHold() {
        return hold;
    }

    public void setHold(String hold) {
        this.hold = hold;
    }
    public String getShipped() {
        return shipped;
    }

    public void setShipped(String shipped) {
        this.shipped = shipped;
    }
    public String getClosed() {
        return closed;
    }

    public void setClosed(String closed) {
        this.closed = closed;
    }


}