





import java.util.List;
import java.util.ArrayList;

public class CarRentalModel_Automobile extends Craft {

    private boolean isCabrio;



    public CarRentalModel_Automobile(
        boolean isCabrio    ) {
        super(
        );
        this.isCabrio = isCabrio;
    }


    public boolean getIscabrio() {
        return isCabrio;
    }

    public void setIscabrio(boolean isCabrio) {
        this.isCabrio = isCabrio;
    }


}