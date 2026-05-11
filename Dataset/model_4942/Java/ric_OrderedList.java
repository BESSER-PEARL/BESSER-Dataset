





import java.util.List;
import java.util.ArrayList;

public class ric_OrderedList extends List {

    private String type;



    public ric_OrderedList(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}