





import java.util.List;
import java.util.ArrayList;

public class shr5Management_LifeModulesSystem extends Shr5System {

    private int knowlegeSkillMax;





    private List<shr5Management_LifeModule> shr5management_lifemodules;


    public shr5Management_LifeModulesSystem(
        int knowlegeSkillMax    ) {
        super(
        );
        this.knowlegeSkillMax = knowlegeSkillMax;
        this.shr5management_lifemodules = new ArrayList<>();
    }

    public shr5Management_LifeModulesSystem(
        int knowlegeSkillMax        ArrayList<shr5Management_LifeModule> shr5management_lifemodules    ) {
        this.knowlegeSkillMax = knowlegeSkillMax;
        this.shr5management_lifemodules = shr5management_lifemodules;
    }

    public int getKnowlegeskillmax() {
        return knowlegeSkillMax;
    }

    public void setKnowlegeskillmax(int knowlegeSkillMax) {
        this.knowlegeSkillMax = knowlegeSkillMax;
    }

    public List<shr5Management_LifeModule> getShr5management_lifemodules() {
        return shr5management_lifemodules;
    }

    public void addShr5management_lifemodule(Shr5management_lifemodule shr5management_lifemodule) {
        this.shr5management_lifemodules.add(shr5management_lifemodule);
    }

}