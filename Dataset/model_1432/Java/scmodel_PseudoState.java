





import java.util.List;
import java.util.ArrayList;

public class scmodel_PseudoState extends AbstractState {

    private String type;



    public scmodel_PseudoState(
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