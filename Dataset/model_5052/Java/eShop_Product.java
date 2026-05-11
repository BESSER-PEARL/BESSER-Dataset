





import java.util.List;
import java.util.ArrayList;

public class eShop_Product  {

    private int price;
    private int stock;





    private List<eShop_SaleLine> eshop_salelines;




    private eShop_SaleLine eshop_saleline;


    public eShop_Product(
        int price,        int stock    ) {
        this.price = price;
        this.stock = stock;
        this.eshop_salelines = new ArrayList<>();
    }

    public eShop_Product(
        int price,        int stock        ArrayList<eShop_SaleLine> eshop_salelines    ) {
        this.price = price;
        this.stock = stock;
        this.eshop_salelines = eshop_salelines;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    public List<eShop_SaleLine> getEshop_salelines() {
        return eshop_salelines;
    }

    public void addEshop_saleline(Eshop_saleline eshop_saleline) {
        this.eshop_salelines.add(eshop_saleline);
    }
    public eShop_SaleLine getEshop_saleline() {
        return eshop_saleline;
    }

    public void setEshop_saleline(eShop_SaleLine eshop_saleline) {
        this.eshop_saleline = eshop_saleline;
    }

}