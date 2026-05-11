





import java.util.List;
import java.util.ArrayList;

public class abs_Mexp  {

    private int value;





    private abs_Feature_decl_constraint abs_feature_decl_constraint;


    public abs_Mexp(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public abs_Feature_decl_constraint getAbs_feature_decl_constraint() {
        return abs_feature_decl_constraint;
    }

    public void setAbs_feature_decl_constraint(abs_Feature_decl_constraint abs_feature_decl_constraint) {
        this.abs_feature_decl_constraint = abs_feature_decl_constraint;
    }

}