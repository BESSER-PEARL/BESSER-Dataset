





import java.util.List;
import java.util.ArrayList;

public class pyrep_DataMove extends Entity {

    private boolean name;
    private String velocity;
    private String type;



    public pyrep_DataMove(
        boolean name,        String velocity,        String type    ) {
        super(
        );
        this.name = name;
        this.velocity = velocity;
        this.type = type;
    }


    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }
    public String getVelocity() {
        return velocity;
    }

    public void setVelocity(String velocity) {
        this.velocity = velocity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}