





import java.util.List;
import java.util.ArrayList;

public class sql_OrderByColumnFull extends OrOrderByColumn {

    private String colOrderInt;
    private String direction;



    public sql_OrderByColumnFull(
        String colOrderInt,        String direction    ) {
        super(
        );
        this.colOrderInt = colOrderInt;
        this.direction = direction;
    }


    public String getColorderint() {
        return colOrderInt;
    }

    public void setColorderint(String colOrderInt) {
        this.colOrderInt = colOrderInt;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}