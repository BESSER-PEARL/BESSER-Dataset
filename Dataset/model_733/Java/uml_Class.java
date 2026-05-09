





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends BehavioredClassifier, EncapsulatedClassifier {

    private String isActive;



    public uml_Class(
        String isActive    ) {
        super(
        );
        this.isActive = isActive;
    }


    public String getIsactive() {
        return isActive;
    }

    public void setIsactive(String isActive) {
        this.isActive = isActive;
    }


}