





import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdBilling_Bill  {

    private boolean isPaid;
    private String ID;



    public Classes_mdsdBilling_Bill(
        boolean isPaid,        String ID    ) {
        this.isPaid = isPaid;
        this.ID = ID;
    }


    public boolean getIspaid() {
        return isPaid;
    }

    public void setIspaid(boolean isPaid) {
        this.isPaid = isPaid;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}