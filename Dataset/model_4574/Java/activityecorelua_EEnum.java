





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EEnum extends EDataType {






    private List<activityecorelua_EEnumLiteral> activityecorelua_eenumliterals;




    private activityecorelua_EEnumLiteral activityecorelua_eenumliteral;


    public activityecorelua_EEnum(
    ) {
        super(
        );
        this.activityecorelua_eenumliterals = new ArrayList<>();
    }

    public activityecorelua_EEnum(
        ArrayList<activityecorelua_EEnumLiteral> activityecorelua_eenumliterals    ) {
        this.activityecorelua_eenumliterals = activityecorelua_eenumliterals;
    }


    public List<activityecorelua_EEnumLiteral> getActivityecorelua_eenumliterals() {
        return activityecorelua_eenumliterals;
    }

    public void addActivityecorelua_eenumliteral(Activityecorelua_eenumliteral activityecorelua_eenumliteral) {
        this.activityecorelua_eenumliterals.add(activityecorelua_eenumliteral);
    }
    public activityecorelua_EEnumLiteral getActivityecorelua_eenumliteral() {
        return activityecorelua_eenumliteral;
    }

    public void setActivityecorelua_eenumliteral(activityecorelua_EEnumLiteral activityecorelua_eenumliteral) {
        this.activityecorelua_eenumliteral = activityecorelua_eenumliteral;
    }

}