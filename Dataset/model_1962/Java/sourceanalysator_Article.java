





import java.util.List;
import java.util.ArrayList;

public class sourceanalysator_Article  {

    private String title;
    private String localFile;





    private sourceanalysator_Source sourceanalysator_source;




    private List<sourceanalysator_Source> sourceanalysator_sources;


    public sourceanalysator_Article(
        String title,        String localFile    ) {
        this.title = title;
        this.localFile = localFile;
        this.sourceanalysator_sources = new ArrayList<>();
    }

    public sourceanalysator_Article(
        String title,        String localFile        ArrayList<sourceanalysator_Source> sourceanalysator_sources    ) {
        this.title = title;
        this.localFile = localFile;
        this.sourceanalysator_sources = sourceanalysator_sources;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLocalfile() {
        return localFile;
    }

    public void setLocalfile(String localFile) {
        this.localFile = localFile;
    }

    public sourceanalysator_Source getSourceanalysator_source() {
        return sourceanalysator_source;
    }

    public void setSourceanalysator_source(sourceanalysator_Source sourceanalysator_source) {
        this.sourceanalysator_source = sourceanalysator_source;
    }
    public List<sourceanalysator_Source> getSourceanalysator_sources() {
        return sourceanalysator_sources;
    }

    public void addSourceanalysator_source(Sourceanalysator_source sourceanalysator_source) {
        this.sourceanalysator_sources.add(sourceanalysator_source);
    }

}