





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_SystemCursor extends Cursor {

    private String type;



    public VisualInterface_SystemCursor(
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