





import java.util.List;
import java.util.ArrayList;

public class Buyer  {

    private String buyer_id;





    private List<Property> propertys;


    public Buyer(
        String buyer_id    ) {
        this.buyer_id = buyer_id;
        this.propertys = new ArrayList<>();
    }

    public Buyer(
        String buyer_id        ArrayList<Property> propertys    ) {
        this.buyer_id = buyer_id;
        this.propertys = propertys;
    }

    public String getBuyer_id() {
        return buyer_id;
    }

    public void setBuyer_id(String buyer_id) {
        this.buyer_id = buyer_id;
    }

    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}