





import java.util.List;
import java.util.ArrayList;

public class vql_Parameter extends Variable {

    private String direction;



    public vql_Parameter(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}