





import java.util.List;
import java.util.ArrayList;

public class UMLModel_LinkEndDestructionData extends LinkEndData {

    private String destroyAt;
    private String isDestroyDuplicates;



    public UMLModel_LinkEndDestructionData(
        String destroyAt,        String isDestroyDuplicates    ) {
        super(
        );
        this.destroyAt = destroyAt;
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


    public String getDestroyat() {
        return destroyAt;
    }

    public void setDestroyat(String destroyAt) {
        this.destroyAt = destroyAt;
    }
    public String getIsdestroyduplicates() {
        return isDestroyDuplicates;
    }

    public void setIsdestroyduplicates(String isDestroyDuplicates) {
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


}