





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_FindHome extends SequenceCommand {

    private String axis;



    public farmbot_modeling_FindHome(
        String axis    ) {
        super(
        );
        this.axis = axis;
    }


    public String getAxis() {
        return axis;
    }

    public void setAxis(String axis) {
        this.axis = axis;
    }


}