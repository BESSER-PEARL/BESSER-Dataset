





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_DataMove extends Entity {

    private String type;
    private String velocity;
    private boolean name;



    public PyDslRep_DataMove(
        String type,        String velocity,        boolean name    ) {
        super(
        );
        this.type = type;
        this.velocity = velocity;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVelocity() {
        return velocity;
    }

    public void setVelocity(String velocity) {
        this.velocity = velocity;
    }
    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }


}