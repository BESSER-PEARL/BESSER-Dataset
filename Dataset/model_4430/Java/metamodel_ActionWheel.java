





import java.util.List;
import java.util.ArrayList;

public class metamodel_ActionWheel extends Action {

    private int speed;





    private metamodel_Group metamodel_group;


    public metamodel_ActionWheel(
        int speed    ) {
        super(
        );
        this.speed = speed;
    }


    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public metamodel_Group getMetamodel_group() {
        return metamodel_group;
    }

    public void setMetamodel_group(metamodel_Group metamodel_group) {
        this.metamodel_group = metamodel_group;
    }

}