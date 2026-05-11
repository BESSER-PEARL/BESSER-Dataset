





import java.util.List;
import java.util.ArrayList;

public class shr5Management_SpecialType extends PriorityCategorie {

    private int skillValue;
    private int skillNumber;



    public shr5Management_SpecialType(
        int skillValue,        int skillNumber    ) {
        super(
        );
        this.skillValue = skillValue;
        this.skillNumber = skillNumber;
    }


    public int getSkillvalue() {
        return skillValue;
    }

    public void setSkillvalue(int skillValue) {
        this.skillValue = skillValue;
    }
    public int getSkillnumber() {
        return skillNumber;
    }

    public void setSkillnumber(int skillNumber) {
        this.skillNumber = skillNumber;
    }


}