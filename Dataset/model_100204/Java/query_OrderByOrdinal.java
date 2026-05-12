





import java.util.List;
import java.util.ArrayList;

public class query_OrderByOrdinal extends OrderBySpecification {

    private int ordinalValue;



    public query_OrderByOrdinal(
        int ordinalValue    ) {
        super(
        );
        this.ordinalValue = ordinalValue;
    }


    public int getOrdinalvalue() {
        return ordinalValue;
    }

    public void setOrdinalvalue(int ordinalValue) {
        this.ordinalValue = ordinalValue;
    }


}