





import java.util.List;
import java.util.ArrayList;

public class tracker_BovineBison extends Bovine {

    private String buffaloBreed;



    public tracker_BovineBison(
        String buffaloBreed    ) {
        super(
        );
        this.buffaloBreed = buffaloBreed;
    }


    public String getBuffalobreed() {
        return buffaloBreed;
    }

    public void setBuffalobreed(String buffaloBreed) {
        this.buffaloBreed = buffaloBreed;
    }


}