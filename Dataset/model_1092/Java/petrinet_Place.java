





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Element {

    private int jetons;



    public petrinet_Place(
        int jetons    ) {
        super(
        );
        this.jetons = jetons;
    }


    public int getJetons() {
        return jetons;
    }

    public void setJetons(int jetons) {
        this.jetons = jetons;
    }


}