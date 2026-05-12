





import java.util.List;
import java.util.ArrayList;

public class Skill  {

    private String skillName;
    private String description;
    private int skillId;
    private String category;
    private int estimatedDuration;
    private None skillLevel;





    private List<UserSkill> userskills;


    public Skill(
        String skillName,        String description,        int skillId,        String category,        int estimatedDuration,        None skillLevel    ) {
        this.skillName = skillName;
        this.description = description;
        this.skillId = skillId;
        this.category = category;
        this.estimatedDuration = estimatedDuration;
        this.skillLevel = skillLevel;
        this.userskills = new ArrayList<>();
    }

    public Skill(
        String skillName,        String description,        int skillId,        String category,        int estimatedDuration,        None skillLevel        ArrayList<UserSkill> userskills    ) {
        this.skillName = skillName;
        this.description = description;
        this.skillId = skillId;
        this.category = category;
        this.estimatedDuration = estimatedDuration;
        this.skillLevel = skillLevel;
        this.userskills = userskills;
    }

    public String getSkillname() {
        return skillName;
    }

    public void setSkillname(String skillName) {
        this.skillName = skillName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getSkillid() {
        return skillId;
    }

    public void setSkillid(int skillId) {
        this.skillId = skillId;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public int getEstimatedduration() {
        return estimatedDuration;
    }

    public void setEstimatedduration(int estimatedDuration) {
        this.estimatedDuration = estimatedDuration;
    }
    public None getSkilllevel() {
        return skillLevel;
    }

    public void setSkilllevel(None skillLevel) {
        this.skillLevel = skillLevel;
    }

    public List<UserSkill> getUserskills() {
        return userskills;
    }

    public void addUserskill(Userskill userskill) {
        this.userskills.add(userskill);
    }

}