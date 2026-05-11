





import java.util.List;
import java.util.ArrayList;

public class dot_Settings extends Statement, AttributedItem {

    private String type;



    public dot_Settings(
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