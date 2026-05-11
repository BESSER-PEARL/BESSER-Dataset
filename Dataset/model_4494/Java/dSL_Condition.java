





import java.util.List;
import java.util.ArrayList;

public class dSL_Condition  {

    private boolean isProbed;
    private boolean collision;
    private boolean not_;
    private boolean atLake;
    private boolean allLakes;





    private dSL_ConditionList dsl_conditionlist;




    private dSL_Condition dsl_condition;


    public dSL_Condition(
        boolean isProbed,        boolean collision,        boolean not_,        boolean atLake,        boolean allLakes    ) {
        this.isProbed = isProbed;
        this.collision = collision;
        this.not_ = not_;
        this.atLake = atLake;
        this.allLakes = allLakes;
    }


    public boolean getIsprobed() {
        return isProbed;
    }

    public void setIsprobed(boolean isProbed) {
        this.isProbed = isProbed;
    }
    public boolean getCollision() {
        return collision;
    }

    public void setCollision(boolean collision) {
        this.collision = collision;
    }
    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public boolean getAtlake() {
        return atLake;
    }

    public void setAtlake(boolean atLake) {
        this.atLake = atLake;
    }
    public boolean getAlllakes() {
        return allLakes;
    }

    public void setAlllakes(boolean allLakes) {
        this.allLakes = allLakes;
    }

    public dSL_ConditionList getDsl_conditionlist() {
        return dsl_conditionlist;
    }

    public void setDsl_conditionlist(dSL_ConditionList dsl_conditionlist) {
        this.dsl_conditionlist = dsl_conditionlist;
    }
    public dSL_Condition getDsl_condition() {
        return dsl_condition;
    }

    public void setDsl_condition(dSL_Condition dsl_condition) {
        this.dsl_condition = dsl_condition;
    }

}