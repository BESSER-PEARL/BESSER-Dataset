





import java.util.List;
import java.util.ArrayList;

public class amazoninformational_Order  {






    private List<amazoninformational_Package> amazoninformational_packages;




    private amazoninformational_Shipment amazoninformational_shipment;




    private amazoninformational_Shipment amazoninformational_shipment;




    private amazoninformational_Invoice amazoninformational_invoice;




    private amazoninformational_Package amazoninformational_package;




    private amazoninformational_Invoice amazoninformational_invoice;


    public amazoninformational_Order(
    ) {
        this.amazoninformational_packages = new ArrayList<>();
    }

    public amazoninformational_Order(
        ArrayList<amazoninformational_Package> amazoninformational_packages    ) {
        this.amazoninformational_packages = amazoninformational_packages;
    }


    public List<amazoninformational_Package> getAmazoninformational_packages() {
        return amazoninformational_packages;
    }

    public void addAmazoninformational_package(Amazoninformational_package amazoninformational_package) {
        this.amazoninformational_packages.add(amazoninformational_package);
    }
    public amazoninformational_Shipment getAmazoninformational_shipment() {
        return amazoninformational_shipment;
    }

    public void setAmazoninformational_shipment(amazoninformational_Shipment amazoninformational_shipment) {
        this.amazoninformational_shipment = amazoninformational_shipment;
    }
    public amazoninformational_Shipment getAmazoninformational_shipment() {
        return amazoninformational_shipment;
    }

    public void setAmazoninformational_shipment(amazoninformational_Shipment amazoninformational_shipment) {
        this.amazoninformational_shipment = amazoninformational_shipment;
    }
    public amazoninformational_Invoice getAmazoninformational_invoice() {
        return amazoninformational_invoice;
    }

    public void setAmazoninformational_invoice(amazoninformational_Invoice amazoninformational_invoice) {
        this.amazoninformational_invoice = amazoninformational_invoice;
    }
    public amazoninformational_Package getAmazoninformational_package() {
        return amazoninformational_package;
    }

    public void setAmazoninformational_package(amazoninformational_Package amazoninformational_package) {
        this.amazoninformational_package = amazoninformational_package;
    }
    public amazoninformational_Invoice getAmazoninformational_invoice() {
        return amazoninformational_invoice;
    }

    public void setAmazoninformational_invoice(amazoninformational_Invoice amazoninformational_invoice) {
        this.amazoninformational_invoice = amazoninformational_invoice;
    }

}