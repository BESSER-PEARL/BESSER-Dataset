





import java.util.List;
import java.util.ArrayList;

public class sample_Scenario  {

    private String Title;





    private sample_Story sample_story;


    public sample_Scenario(
        String Title    ) {
        this.Title = Title;
    }


    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }

    public sample_Story getSample_story() {
        return sample_story;
    }

    public void setSample_story(sample_Story sample_story) {
        this.sample_story = sample_story;
    }

}