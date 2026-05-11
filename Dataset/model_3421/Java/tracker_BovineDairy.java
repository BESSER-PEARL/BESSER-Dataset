





import java.util.List;
import java.util.ArrayList;

public class tracker_BovineDairy extends Bovine {

    private String dairyBreed;



    public tracker_BovineDairy(
        String dairyBreed    ) {
        super(
        );
        this.dairyBreed = dairyBreed;
    }


    public String getDairybreed() {
        return dairyBreed;
    }

    public void setDairybreed(String dairyBreed) {
        this.dairyBreed = dairyBreed;
    }


}