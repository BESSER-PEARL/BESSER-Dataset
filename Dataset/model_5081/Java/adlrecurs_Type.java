





import java.util.List;
import java.util.ArrayList;

public class adlrecurs_Type extends Interface {

    private String signature;





    private List<adlrecurs_Item> adlrecurs_items;


    public adlrecurs_Type(
        String signature    ) {
        super(
        );
        this.signature = signature;
        this.adlrecurs_items = new ArrayList<>();
    }

    public adlrecurs_Type(
        String signature        ArrayList<adlrecurs_Item> adlrecurs_items    ) {
        this.signature = signature;
        this.adlrecurs_items = adlrecurs_items;
    }

    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public List<adlrecurs_Item> getAdlrecurs_items() {
        return adlrecurs_items;
    }

    public void addAdlrecurs_item(Adlrecurs_item adlrecurs_item) {
        this.adlrecurs_items.add(adlrecurs_item);
    }

}