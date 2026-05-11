





import java.util.List;
import java.util.ArrayList;

public class behaviour_GoTo extends Move {

    private String strategy;



    public behaviour_GoTo(
        String strategy    ) {
        super(
        );
        this.strategy = strategy;
    }


    public String getStrategy() {
        return strategy;
    }

    public void setStrategy(String strategy) {
        this.strategy = strategy;
    }


}