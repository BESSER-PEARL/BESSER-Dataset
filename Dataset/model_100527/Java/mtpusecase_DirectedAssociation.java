





import java.util.List;
import java.util.ArrayList;

public class mtpusecase_DirectedAssociation extends Relation {

    private String targetName;



    public mtpusecase_DirectedAssociation(
        String targetName    ) {
        super(
        );
        this.targetName = targetName;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }


}