





import java.util.List;
import java.util.ArrayList;

public class Promos  {

    private String PromoCode;
    private String Name;
    private String StartDate;
    private String Discount;
    private String EndDate;





    private Premium_Members premium_members;




    private List<ShoppingCart> shoppingcarts;


    public Promos(
        String PromoCode,        String Name,        String StartDate,        String Discount,        String EndDate    ) {
        this.PromoCode = PromoCode;
        this.Name = Name;
        this.StartDate = StartDate;
        this.Discount = Discount;
        this.EndDate = EndDate;
        this.shoppingcarts = new ArrayList<>();
    }

    public Promos(
        String PromoCode,        String Name,        String StartDate,        String Discount,        String EndDate        ArrayList<ShoppingCart> shoppingcarts    ) {
        this.PromoCode = PromoCode;
        this.Name = Name;
        this.StartDate = StartDate;
        this.Discount = Discount;
        this.EndDate = EndDate;
        this.shoppingcarts = shoppingcarts;
    }

    public String getPromocode() {
        return PromoCode;
    }

    public void setPromocode(String PromoCode) {
        this.PromoCode = PromoCode;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getStartdate() {
        return StartDate;
    }

    public void setStartdate(String StartDate) {
        this.StartDate = StartDate;
    }
    public String getDiscount() {
        return Discount;
    }

    public void setDiscount(String Discount) {
        this.Discount = Discount;
    }
    public String getEnddate() {
        return EndDate;
    }

    public void setEnddate(String EndDate) {
        this.EndDate = EndDate;
    }

    public Premium_Members getPremium_members() {
        return premium_members;
    }

    public void setPremium_members(Premium_Members premium_members) {
        this.premium_members = premium_members;
    }
    public List<ShoppingCart> getShoppingcarts() {
        return shoppingcarts;
    }

    public void addShoppingcart(Shoppingcart shoppingcart) {
        this.shoppingcarts.add(shoppingcart);
    }

}