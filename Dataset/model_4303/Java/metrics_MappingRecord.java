





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRecord extends Base {

    private String message;
    private String count;
    private String column;



    public metrics_MappingRecord(
        String message,        String count,        String column    ) {
        super(
        );
        this.message = message;
        this.count = count;
        this.column = column;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }
    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }


}