





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_UserDefinedTypeOrdering extends SQLObject {

    private String orderingForm;
    private String orderingCategory;



    public sqlmodel_datatypes_UserDefinedTypeOrdering(
        String orderingForm,        String orderingCategory    ) {
        super(
        );
        this.orderingForm = orderingForm;
        this.orderingCategory = orderingCategory;
    }


    public String getOrderingform() {
        return orderingForm;
    }

    public void setOrderingform(String orderingForm) {
        this.orderingForm = orderingForm;
    }
    public String getOrderingcategory() {
        return orderingCategory;
    }

    public void setOrderingcategory(String orderingCategory) {
        this.orderingCategory = orderingCategory;
    }


}