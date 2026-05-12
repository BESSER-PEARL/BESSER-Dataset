





import java.util.List;
import java.util.ArrayList;

public class In_house_Component  {

    private String Manufacture_Product;
    private String Quality;



    public In_house_Component(
        String Manufacture_Product,        String Quality    ) {
        this.Manufacture_Product = Manufacture_Product;
        this.Quality = Quality;
    }


    public String getManufacture_product() {
        return Manufacture_Product;
    }

    public void setManufacture_product(String Manufacture_Product) {
        this.Manufacture_Product = Manufacture_Product;
    }
    public String getQuality() {
        return Quality;
    }

    public void setQuality(String Quality) {
        this.Quality = Quality;
    }


}