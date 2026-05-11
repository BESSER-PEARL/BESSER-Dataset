





import java.util.List;
import java.util.ArrayList;

public class ktest301_Type extends Interface {

    private String signature;





    private List<ktest301_Item> ktest301_items;


    public ktest301_Type(
        String signature    ) {
        super(
        );
        this.signature = signature;
        this.ktest301_items = new ArrayList<>();
    }

    public ktest301_Type(
        String signature        ArrayList<ktest301_Item> ktest301_items    ) {
        this.signature = signature;
        this.ktest301_items = ktest301_items;
    }

    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public List<ktest301_Item> getKtest301_items() {
        return ktest301_items;
    }

    public void addKtest301_item(Ktest301_item ktest301_item) {
        this.ktest301_items.add(ktest301_item);
    }

}