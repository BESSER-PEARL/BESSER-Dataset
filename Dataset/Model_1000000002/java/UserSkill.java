





import java.util.List;
import java.util.ArrayList;

public class UserSkill  {

    private int yearsOfExperience;
    private None skillLevel;
    private boolean certification;
    private int skillId;





    private User user;


    public UserSkill(
        int yearsOfExperience,        None skillLevel,        boolean certification,        int skillId    ) {
        this.yearsOfExperience = yearsOfExperience;
        this.skillLevel = skillLevel;
        this.certification = certification;
        this.skillId = skillId;
    }


    public int getYearsofexperience() {
        return yearsOfExperience;
    }

    public void setYearsofexperience(int yearsOfExperience) {
        this.yearsOfExperience = yearsOfExperience;
    }
    public None getSkilllevel() {
        return skillLevel;
    }

    public void setSkilllevel(None skillLevel) {
        this.skillLevel = skillLevel;
    }
    public boolean getCertification() {
        return certification;
    }

    public void setCertification(boolean certification) {
        this.certification = certification;
    }
    public int getSkillid() {
        return skillId;
    }

    public void setSkillid(int skillId) {
        this.skillId = skillId;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}