





import java.util.List;
import java.util.ArrayList;

public class eShop_Customer  {

    private int name;





    private eShop_Sale eshop_sale;




    private List<eShop_Sale> eshop_sales;


    public eShop_Customer(
        int name    ) {
        this.name = name;
        this.eshop_sales = new ArrayList<>();
    }

    public eShop_Customer(
        int name        ArrayList<eShop_Sale> eshop_sales    ) {
        this.name = name;
        this.eshop_sales = eshop_sales;
    }

    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }

    public eShop_Sale getEshop_sale() {
        return eshop_sale;
    }

    public void setEshop_sale(eShop_Sale eshop_sale) {
        this.eshop_sale = eshop_sale;
    }
    public List<eShop_Sale> getEshop_sales() {
        return eshop_sales;
    }

    public void addEshop_sale(Eshop_sale eshop_sale) {
        this.eshop_sales.add(eshop_sale);
    }

}