





import java.util.List;
import java.util.ArrayList;

public class DB_Column extends DatabaseElement {

    private String type;



    public DB_Column(
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