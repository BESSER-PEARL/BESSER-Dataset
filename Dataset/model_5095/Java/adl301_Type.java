





import java.util.List;
import java.util.ArrayList;

public class adl301_Type extends Interface {

    private String signature;





    private List<adl301_Item> adl301_items;


    public adl301_Type(
        String signature    ) {
        super(
        );
        this.signature = signature;
        this.adl301_items = new ArrayList<>();
    }

    public adl301_Type(
        String signature        ArrayList<adl301_Item> adl301_items    ) {
        this.signature = signature;
        this.adl301_items = adl301_items;
    }

    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public List<adl301_Item> getAdl301_items() {
        return adl301_items;
    }

    public void addAdl301_item(Adl301_item adl301_item) {
        this.adl301_items.add(adl301_item);
    }

}