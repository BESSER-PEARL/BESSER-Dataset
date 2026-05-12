





import java.util.List;
import java.util.ArrayList;

public class Bill  {






    private List<Discount> discounts;


    public Bill(
    ) {
        this.discounts = new ArrayList<>();
    }

    public Bill(
        ArrayList<Discount> discounts    ) {
        this.discounts = discounts;
    }


    public List<Discount> getDiscounts() {
        return discounts;
    }

    public void addDiscount(Discount discount) {
        this.discounts.add(discount);
    }

}