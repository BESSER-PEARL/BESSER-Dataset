





import java.util.List;
import java.util.ArrayList;

public class statemachine_GStatemachine extends GCompositeState {

    private String package;



    public statemachine_GStatemachine(
        String package    ) {
        super(
        );
        this.package = package;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }


}