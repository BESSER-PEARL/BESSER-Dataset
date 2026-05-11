





import java.util.List;
import java.util.ArrayList;

public class dsl_Unit  {

    private int sight;
    private String radius;
    private String uIName;
    private String speed;
    private String separationRadius;
    private int maxHealth;
    private String name;
    private String mass;





    private dsl_Model dsl_model;




    private dsl_Mover dsl_mover;


    public dsl_Unit(
        int sight,        String radius,        String uIName,        String speed,        String separationRadius,        int maxHealth,        String name,        String mass    ) {
        this.sight = sight;
        this.radius = radius;
        this.uIName = uIName;
        this.speed = speed;
        this.separationRadius = separationRadius;
        this.maxHealth = maxHealth;
        this.name = name;
        this.mass = mass;
    }


    public int getSight() {
        return sight;
    }

    public void setSight(int sight) {
        this.sight = sight;
    }
    public String getRadius() {
        return radius;
    }

    public void setRadius(String radius) {
        this.radius = radius;
    }
    public String getUiname() {
        return uIName;
    }

    public void setUiname(String uIName) {
        this.uIName = uIName;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getSeparationradius() {
        return separationRadius;
    }

    public void setSeparationradius(String separationRadius) {
        this.separationRadius = separationRadius;
    }
    public int getMaxhealth() {
        return maxHealth;
    }

    public void setMaxhealth(int maxHealth) {
        this.maxHealth = maxHealth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMass() {
        return mass;
    }

    public void setMass(String mass) {
        this.mass = mass;
    }

    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }
    public dsl_Mover getDsl_mover() {
        return dsl_mover;
    }

    public void setDsl_mover(dsl_Mover dsl_mover) {
        this.dsl_mover = dsl_mover;
    }

}