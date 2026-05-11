





import java.util.List;
import java.util.ArrayList;

public class r1_Last extends Expression {

    private String orderBy;



    public r1_Last(
        String orderBy    ) {
        super(
        );
        this.orderBy = orderBy;
    }


    public String getOrderby() {
        return orderBy;
    }

    public void setOrderby(String orderBy) {
        this.orderBy = orderBy;
    }


}