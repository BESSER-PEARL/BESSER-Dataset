





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRecord extends Base {

    private String count;
    private String message;
    private String column;



    public metrics_MappingRecord(
        String count,        String message,        String column    ) {
        super(
        );
        this.count = count;
        this.message = message;
        this.column = column;
    }


    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }


}