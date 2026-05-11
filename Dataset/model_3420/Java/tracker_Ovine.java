





import java.util.List;
import java.util.ArrayList;

public class tracker_Ovine extends Animal {

    private String sheepBreed;



    public tracker_Ovine(
        String sheepBreed    ) {
        super(
        );
        this.sheepBreed = sheepBreed;
    }


    public String getSheepbreed() {
        return sheepBreed;
    }

    public void setSheepbreed(String sheepBreed) {
        this.sheepBreed = sheepBreed;
    }


}