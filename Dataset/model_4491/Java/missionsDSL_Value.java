





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_Value  {

    private int integer;
    private String bool;
    private String color;





    private missionsDSL_Condition missionsdsl_condition;


    public missionsDSL_Value(
        int integer,        String bool,        String color    ) {
        this.integer = integer;
        this.bool = bool;
        this.color = color;
    }


    public int getInteger() {
        return integer;
    }

    public void setInteger(int integer) {
        this.integer = integer;
    }
    public String getBool() {
        return bool;
    }

    public void setBool(String bool) {
        this.bool = bool;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public missionsDSL_Condition getMissionsdsl_condition() {
        return missionsdsl_condition;
    }

    public void setMissionsdsl_condition(missionsDSL_Condition missionsdsl_condition) {
        this.missionsdsl_condition = missionsdsl_condition;
    }

}