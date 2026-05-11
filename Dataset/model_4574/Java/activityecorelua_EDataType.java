





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EDataType extends EClassifier {

    private boolean serializable;





    private activityecorelua_EAttribute activityecorelua_eattribute;


    public activityecorelua_EDataType(
        boolean serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public boolean getSerializable() {
        return serializable;
    }

    public void setSerializable(boolean serializable) {
        this.serializable = serializable;
    }

    public activityecorelua_EAttribute getActivityecorelua_eattribute() {
        return activityecorelua_eattribute;
    }

    public void setActivityecorelua_eattribute(activityecorelua_EAttribute activityecorelua_eattribute) {
        this.activityecorelua_eattribute = activityecorelua_eattribute;
    }

}