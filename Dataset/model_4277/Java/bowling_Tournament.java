





import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private String name;
    private String type;





    private bowling_Alley bowling_alley;


    public bowling_Tournament(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public bowling_Alley getBowling_alley() {
        return bowling_alley;
    }

    public void setBowling_alley(bowling_Alley bowling_alley) {
        this.bowling_alley = bowling_alley;
    }

}