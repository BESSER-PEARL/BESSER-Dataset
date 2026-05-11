





import java.util.List;
import java.util.ArrayList;

public class dsl_Projectile  {

    private int mass;
    private String name;
    private int speed;
    private String precision;





    private dsl_Actor dsl_actor;




    private dsl_Mover dsl_mover;




    private dsl_Model dsl_model;


    public dsl_Projectile(
        int mass,        String name,        int speed,        String precision    ) {
        this.mass = mass;
        this.name = name;
        this.speed = speed;
        this.precision = precision;
    }


    public int getMass() {
        return mass;
    }

    public void setMass(int mass) {
        this.mass = mass;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }

    public dsl_Actor getDsl_actor() {
        return dsl_actor;
    }

    public void setDsl_actor(dsl_Actor dsl_actor) {
        this.dsl_actor = dsl_actor;
    }
    public dsl_Mover getDsl_mover() {
        return dsl_mover;
    }

    public void setDsl_mover(dsl_Mover dsl_mover) {
        this.dsl_mover = dsl_mover;
    }
    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }

}