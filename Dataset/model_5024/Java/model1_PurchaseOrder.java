




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model1_PurchaseOrder extends Order {

    private LocalDate date;





    private model1_Supplier model1_supplier;




    private model1_Supplier model1_supplier;


    public model1_PurchaseOrder(
        LocalDate date    ) {
        super(
        );
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public model1_Supplier getModel1_supplier() {
        return model1_supplier;
    }

    public void setModel1_supplier(model1_Supplier model1_supplier) {
        this.model1_supplier = model1_supplier;
    }
    public model1_Supplier getModel1_supplier() {
        return model1_supplier;
    }

    public void setModel1_supplier(model1_Supplier model1_supplier) {
        this.model1_supplier = model1_supplier;
    }

}