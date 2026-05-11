





import java.util.List;
import java.util.ArrayList;

public class shr5Management_LifeModulesGenerator  {

    private int moduleKarmaCost;
    private int startingAge;



    public shr5Management_LifeModulesGenerator(
        int moduleKarmaCost,        int startingAge    ) {
        this.moduleKarmaCost = moduleKarmaCost;
        this.startingAge = startingAge;
    }


    public int getModulekarmacost() {
        return moduleKarmaCost;
    }

    public void setModulekarmacost(int moduleKarmaCost) {
        this.moduleKarmaCost = moduleKarmaCost;
    }
    public int getStartingage() {
        return startingAge;
    }

    public void setStartingage(int startingAge) {
        this.startingAge = startingAge;
    }


}