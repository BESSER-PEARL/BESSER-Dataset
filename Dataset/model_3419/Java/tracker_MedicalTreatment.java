





import java.util.List;
import java.util.ArrayList;

public class tracker_MedicalTreatment extends Event {

    private String name;
    private String lot;
    private String manufacturer;
    private String product;
    private String method;
    private String treatment;
    private String quantity;



    public tracker_MedicalTreatment(
        String name,        String lot,        String manufacturer,        String product,        String method,        String treatment,        String quantity    ) {
        super(
        );
        this.name = name;
        this.lot = lot;
        this.manufacturer = manufacturer;
        this.product = product;
        this.method = method;
        this.treatment = treatment;
        this.quantity = quantity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLot() {
        return lot;
    }

    public void setLot(String lot) {
        this.lot = lot;
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
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getTreatment() {
        return treatment;
    }

    public void setTreatment(String treatment) {
        this.treatment = treatment;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }


}