





import java.util.List;
import java.util.ArrayList;

public class workflow_Read extends Statement {

    private String type;



    public workflow_Read(
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