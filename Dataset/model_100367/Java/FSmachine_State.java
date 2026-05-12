





import java.util.List;
import java.util.ArrayList;

public class FSmachine_State extends AbstractObject {

    private String description;
    private String data;



    public FSmachine_State(
        String description,        String data    ) {
        super(
        );
        this.description = description;
        this.data = data;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}