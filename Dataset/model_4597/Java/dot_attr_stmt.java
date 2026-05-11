





import java.util.List;
import java.util.ArrayList;

public class dot_attr_stmt extends stmt {

    private String type;



    public dot_attr_stmt(
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