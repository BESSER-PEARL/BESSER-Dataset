





import java.util.List;
import java.util.ArrayList;

public class dsl_Effect  {

    private String name;





    private dsl_Weapon dsl_weapon;




    private dsl_Model dsl_model;


    public dsl_Effect(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Weapon getDsl_weapon() {
        return dsl_weapon;
    }

    public void setDsl_weapon(dsl_Weapon dsl_weapon) {
        this.dsl_weapon = dsl_weapon;
    }
    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }

}