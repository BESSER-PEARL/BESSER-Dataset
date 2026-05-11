





import java.util.List;
import java.util.ArrayList;

public class sample_Register  {

    private String Name;





    private List<sample_Story> sample_storys;


    public sample_Register(
        String Name    ) {
        this.Name = Name;
        this.sample_storys = new ArrayList<>();
    }

    public sample_Register(
        String Name        ArrayList<sample_Story> sample_storys    ) {
        this.Name = Name;
        this.sample_storys = sample_storys;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<sample_Story> getSample_storys() {
        return sample_storys;
    }

    public void addSample_story(Sample_story sample_story) {
        this.sample_storys.add(sample_story);
    }

}