





import java.util.List;
import java.util.ArrayList;

public class model1_OrderAddress extends Address, Order, OrderDetail {

    private boolean testAttribute;



    public model1_OrderAddress(
        boolean testAttribute    ) {
        super(
        );
        this.testAttribute = testAttribute;
    }


    public boolean getTestattribute() {
        return testAttribute;
    }

    public void setTestattribute(boolean testAttribute) {
        this.testAttribute = testAttribute;
    }


}