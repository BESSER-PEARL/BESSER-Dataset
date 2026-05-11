





import java.util.List;
import java.util.ArrayList;

public class shr5Management_Skill extends PriorityCategorie {

    private int skillPoints;
    private int groupPoints;



    public shr5Management_Skill(
        int skillPoints,        int groupPoints    ) {
        super(
        );
        this.skillPoints = skillPoints;
        this.groupPoints = groupPoints;
    }


    public int getSkillpoints() {
        return skillPoints;
    }

    public void setSkillpoints(int skillPoints) {
        this.skillPoints = skillPoints;
    }
    public int getGrouppoints() {
        return groupPoints;
    }

    public void setGrouppoints(int groupPoints) {
        this.groupPoints = groupPoints;
    }


}