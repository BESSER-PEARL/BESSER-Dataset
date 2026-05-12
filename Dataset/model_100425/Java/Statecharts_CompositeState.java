





import java.util.List;
import java.util.ArrayList;

public class Statecharts_CompositeState extends State {

    private String isConcurrent;



    public Statecharts_CompositeState(
        String isConcurrent    ) {
        super(
        );
        this.isConcurrent = isConcurrent;
    }


    public String getIsconcurrent() {
        return isConcurrent;
    }

    public void setIsconcurrent(String isConcurrent) {
        this.isConcurrent = isConcurrent;
    }


}