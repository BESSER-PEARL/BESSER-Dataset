





import java.util.List;
import java.util.ArrayList;

public class extralazy_Book  {

    private String subTitles;
    private String title;





    private List<extralazy_Writer> extralazy_writers;


    public extralazy_Book(
        String subTitles,        String title    ) {
        this.subTitles = subTitles;
        this.title = title;
        this.extralazy_writers = new ArrayList<>();
    }

    public extralazy_Book(
        String subTitles,        String title        ArrayList<extralazy_Writer> extralazy_writers    ) {
        this.subTitles = subTitles;
        this.title = title;
        this.extralazy_writers = extralazy_writers;
    }

    public String getSubtitles() {
        return subTitles;
    }

    public void setSubtitles(String subTitles) {
        this.subTitles = subTitles;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<extralazy_Writer> getExtralazy_writers() {
        return extralazy_writers;
    }

    public void addExtralazy_writer(Extralazy_writer extralazy_writer) {
        this.extralazy_writers.add(extralazy_writer);
    }

}