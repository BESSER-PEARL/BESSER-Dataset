





import java.util.List;
import java.util.ArrayList;

public class query_OrderBySpecification extends SQLQueryObject {

    private String OrderingSpecOption;
    private boolean descending;
    private String NullOrderingOption;



    public query_OrderBySpecification(
        String OrderingSpecOption,        boolean descending,        String NullOrderingOption    ) {
        super(
        );
        this.OrderingSpecOption = OrderingSpecOption;
        this.descending = descending;
        this.NullOrderingOption = NullOrderingOption;
    }


    public String getOrderingspecoption() {
        return OrderingSpecOption;
    }

    public void setOrderingspecoption(String OrderingSpecOption) {
        this.OrderingSpecOption = OrderingSpecOption;
    }
    public boolean getDescending() {
        return descending;
    }

    public void setDescending(boolean descending) {
        this.descending = descending;
    }
    public String getNullorderingoption() {
        return NullOrderingOption;
    }

    public void setNullorderingoption(String NullOrderingOption) {
        this.NullOrderingOption = NullOrderingOption;
    }


}