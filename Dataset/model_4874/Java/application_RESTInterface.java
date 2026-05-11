





import java.util.List;
import java.util.ArrayList;

public class application_RESTInterface extends Interface {

    private String type;



    public application_RESTInterface(
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