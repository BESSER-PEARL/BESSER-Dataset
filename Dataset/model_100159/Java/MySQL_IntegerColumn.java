





import java.util.List;
import java.util.ArrayList;

public class MySQL_IntegerColumn extends Column {

    private String isAutoIncrement;



    public MySQL_IntegerColumn(
        String isAutoIncrement    ) {
        super(
        );
        this.isAutoIncrement = isAutoIncrement;
    }


    public String getIsautoincrement() {
        return isAutoIncrement;
    }

    public void setIsautoincrement(String isAutoIncrement) {
        this.isAutoIncrement = isAutoIncrement;
    }


}