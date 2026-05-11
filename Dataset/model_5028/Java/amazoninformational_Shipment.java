





import java.util.List;
import java.util.ArrayList;

public class amazoninformational_Shipment  {






    private amazoninformational_Order amazoninformational_order;




    private List<amazoninformational_Package> amazoninformational_packages;




    private amazoninformational_Order amazoninformational_order;


    public amazoninformational_Shipment(
    ) {
        this.amazoninformational_packages = new ArrayList<>();
    }

    public amazoninformational_Shipment(
        ArrayList<amazoninformational_Package> amazoninformational_packages    ) {
        this.amazoninformational_packages = amazoninformational_packages;
    }


    public amazoninformational_Order getAmazoninformational_order() {
        return amazoninformational_order;
    }

    public void setAmazoninformational_order(amazoninformational_Order amazoninformational_order) {
        this.amazoninformational_order = amazoninformational_order;
    }
    public List<amazoninformational_Package> getAmazoninformational_packages() {
        return amazoninformational_packages;
    }

    public void addAmazoninformational_package(Amazoninformational_package amazoninformational_package) {
        this.amazoninformational_packages.add(amazoninformational_package);
    }
    public amazoninformational_Order getAmazoninformational_order() {
        return amazoninformational_order;
    }

    public void setAmazoninformational_order(amazoninformational_Order amazoninformational_order) {
        this.amazoninformational_order = amazoninformational_order;
    }

}