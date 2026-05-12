





import java.util.List;
import java.util.ArrayList;

public class urml_goal_Goal extends UrmlModelElement {

    private String type;
    private boolean soft;



    public urml_goal_Goal(
        String type,        boolean soft    ) {
        super(
        );
        this.type = type;
        this.soft = soft;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getSoft() {
        return soft;
    }

    public void setSoft(boolean soft) {
        this.soft = soft;
    }


}