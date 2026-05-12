





import java.util.List;
import java.util.ArrayList;

public class APNModel  {






    private List<APNLineItem> apnlineitems;




    private APNLineItem apnlineitem;




    private List<APNAdvertiser> apnadvertisers;


    public APNModel(
    ) {
        this.apnlineitems = new ArrayList<>();
        this.apnadvertisers = new ArrayList<>();
    }

    public APNModel(
        ArrayList<APNLineItem> apnlineitems,        ArrayList<APNAdvertiser> apnadvertisers    ) {
        this.apnlineitems = apnlineitems;
        this.apnadvertisers = apnadvertisers;
    }


    public List<APNLineItem> getApnlineitems() {
        return apnlineitems;
    }

    public void addApnlineitem(Apnlineitem apnlineitem) {
        this.apnlineitems.add(apnlineitem);
    }
    public APNLineItem getApnlineitem() {
        return apnlineitem;
    }

    public void setApnlineitem(APNLineItem apnlineitem) {
        this.apnlineitem = apnlineitem;
    }
    public List<APNAdvertiser> getApnadvertisers() {
        return apnadvertisers;
    }

    public void addApnadvertiser(Apnadvertiser apnadvertiser) {
        this.apnadvertisers.add(apnadvertiser);
    }

}