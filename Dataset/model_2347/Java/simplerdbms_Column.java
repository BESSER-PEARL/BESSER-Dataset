





import java.util.List;
import java.util.ArrayList;

public class simplerdbms_Column extends RModelElement {

    private String type;



    public simplerdbms_Column(
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