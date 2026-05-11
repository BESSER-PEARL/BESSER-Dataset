





import java.util.List;
import java.util.ArrayList;

public class relational_Column extends Field {

    private String type;



    public relational_Column(
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