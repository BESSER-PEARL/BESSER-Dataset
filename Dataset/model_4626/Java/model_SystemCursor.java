





import java.util.List;
import java.util.ArrayList;

public class model_SystemCursor extends Cursor {

    private String type;



    public model_SystemCursor(
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