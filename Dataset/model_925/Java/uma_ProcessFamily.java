





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessFamily extends MethodConfiguration {






    private List<uma_DeliveryProcess> uma_deliveryprocesss;


    public uma_ProcessFamily(
    ) {
        super(
        );
        this.uma_deliveryprocesss = new ArrayList<>();
    }

    public uma_ProcessFamily(
        ArrayList<uma_DeliveryProcess> uma_deliveryprocesss    ) {
        this.uma_deliveryprocesss = uma_deliveryprocesss;
    }


    public List<uma_DeliveryProcess> getUma_deliveryprocesss() {
        return uma_deliveryprocesss;
    }

    public void addUma_deliveryprocess(Uma_deliveryprocess uma_deliveryprocess) {
        this.uma_deliveryprocesss.add(uma_deliveryprocess);
    }

}