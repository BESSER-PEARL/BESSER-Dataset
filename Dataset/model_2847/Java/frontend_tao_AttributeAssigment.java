





import java.util.List;
import java.util.ArrayList;

public class frontend_tao_AttributeAssigment extends Assignment {

    private String targetFeature;



    public frontend_tao_AttributeAssigment(
        String targetFeature    ) {
        super(
        );
        this.targetFeature = targetFeature;
    }


    public String getTargetfeature() {
        return targetFeature;
    }

    public void setTargetfeature(String targetFeature) {
        this.targetFeature = targetFeature;
    }


}