





import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_VipCustomer extends Customer {

    private float discount;



    public CarRentalModel_VipCustomer(
        float discount    ) {
        super(
        );
        this.discount = discount;
    }


    public float getDiscount() {
        return discount;
    }

    public void setDiscount(float discount) {
        this.discount = discount;
    }


}