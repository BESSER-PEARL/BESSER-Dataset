





import java.util.List;
import java.util.ArrayList;

public class ordersystem_special_LimitedEditionProduct extends Product {

    private String availableUntil;



    public ordersystem_special_LimitedEditionProduct(
        String availableUntil    ) {
        super(
        );
        this.availableUntil = availableUntil;
    }


    public String getAvailableuntil() {
        return availableUntil;
    }

    public void setAvailableuntil(String availableUntil) {
        this.availableUntil = availableUntil;
    }


}