





import java.util.List;
import java.util.ArrayList;

public class dsl_LauncherEffect extends Effect {






    private List<dsl_Projectile> dsl_projectiles;




    private List<dsl_Effect> dsl_effects;


    public dsl_LauncherEffect(
    ) {
        super(
        );
        this.dsl_projectiles = new ArrayList<>();
        this.dsl_effects = new ArrayList<>();
    }

    public dsl_LauncherEffect(
        ArrayList<dsl_Projectile> dsl_projectiles,        ArrayList<dsl_Effect> dsl_effects    ) {
        this.dsl_projectiles = dsl_projectiles;
        this.dsl_effects = dsl_effects;
    }


    public List<dsl_Projectile> getDsl_projectiles() {
        return dsl_projectiles;
    }

    public void addDsl_projectile(Dsl_projectile dsl_projectile) {
        this.dsl_projectiles.add(dsl_projectile);
    }
    public List<dsl_Effect> getDsl_effects() {
        return dsl_effects;
    }

    public void addDsl_effect(Dsl_effect dsl_effect) {
        this.dsl_effects.add(dsl_effect);
    }

}