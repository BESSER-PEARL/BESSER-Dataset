





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_Column extends RModelElement {

    private String type;



    public rdbmsMM_Column(
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