





import java.util.List;
import java.util.ArrayList;

public class tracker_Equine extends Animal {

    private String horseBreed;



    public tracker_Equine(
        String horseBreed    ) {
        super(
        );
        this.horseBreed = horseBreed;
    }


    public String getHorsebreed() {
        return horseBreed;
    }

    public void setHorsebreed(String horseBreed) {
        this.horseBreed = horseBreed;
    }


}