





import java.util.List;
import java.util.ArrayList;

public class WeaponAttack  {

    private None weapon;
    private String execute__;



    public WeaponAttack(
        None weapon,        String execute__    ) {
        this.weapon = weapon;
        this.execute__ = execute__;
    }


    public None getWeapon() {
        return weapon;
    }

    public void setWeapon(None weapon) {
        this.weapon = weapon;
    }
    public String getExecute__() {
        return execute__;
    }

    public void setExecute__(String execute__) {
        this.execute__ = execute__;
    }


}