





import java.util.List;
import java.util.ArrayList;

public class simulink_MiscBlock extends Block {

    private String type;



    public simulink_MiscBlock(
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