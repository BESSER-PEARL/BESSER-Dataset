





import java.util.List;
import java.util.ArrayList;

public class express_algorithms_Parameter extends LocalElement {

    private String inout;
    private String position;



    public express_algorithms_Parameter(
        String inout,        String position    ) {
        super(
        );
        this.inout = inout;
        this.position = position;
    }


    public String getInout() {
        return inout;
    }

    public void setInout(String inout) {
        this.inout = inout;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}