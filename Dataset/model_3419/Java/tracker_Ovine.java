





import java.util.List;
import java.util.ArrayList;

public class tracker_Ovine extends Animal {

    private String scrapieTag;
    private String sheepBreed;



    public tracker_Ovine(
        String scrapieTag,        String sheepBreed    ) {
        super(
        );
        this.scrapieTag = scrapieTag;
        this.sheepBreed = sheepBreed;
    }


    public String getScrapietag() {
        return scrapieTag;
    }

    public void setScrapietag(String scrapieTag) {
        this.scrapieTag = scrapieTag;
    }
    public String getSheepbreed() {
        return sheepBreed;
    }

    public void setSheepbreed(String sheepBreed) {
        this.sheepBreed = sheepBreed;
    }


}