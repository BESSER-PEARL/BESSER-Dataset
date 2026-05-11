





import java.util.List;
import java.util.ArrayList;

public class tracker_MedicalTreatment extends Event {

    private String method;
    private String name;
    private String manufacturer;
    private String product;
    private String lot;
    private String quantity;
    private String treatment;



    public tracker_MedicalTreatment(
        String method,        String name,        String manufacturer,        String product,        String lot,        String quantity,        String treatment    ) {
        super(
        );
        this.method = method;
        this.name = name;
        this.manufacturer = manufacturer;
        this.product = product;
        this.lot = lot;
        this.quantity = quantity;
        this.treatment = treatment;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }
    public String getProduct() {
        return product;
    }

    public void setProduct(String product) {
        this.product = product;
    }
    public String getLot() {
        return lot;
    }

    public void setLot(String lot) {
        this.lot = lot;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getTreatment() {
        return treatment;
    }

    public void setTreatment(String treatment) {
        this.treatment = treatment;
    }


}