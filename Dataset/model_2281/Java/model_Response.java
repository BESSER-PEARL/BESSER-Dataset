





import java.util.List;
import java.util.ArrayList;

public class model_Response  {

    private int ID;
    private boolean ok;
    private String comment;





    private model_Delivery model_delivery;


    public model_Response(
        int ID,        boolean ok,        String comment    ) {
        this.ID = ID;
        this.ok = ok;
        this.comment = comment;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public boolean getOk() {
        return ok;
    }

    public void setOk(boolean ok) {
        this.ok = ok;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public model_Delivery getModel_delivery() {
        return model_delivery;
    }

    public void setModel_delivery(model_Delivery model_delivery) {
        this.model_delivery = model_delivery;
    }

}