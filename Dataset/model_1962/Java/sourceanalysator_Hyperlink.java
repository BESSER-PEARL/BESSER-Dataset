





import java.util.List;
import java.util.ArrayList;

public class sourceanalysator_Hyperlink  {

    private String url;





    private sourceanalysator_Source sourceanalysator_source;




    private List<sourceanalysator_Source> sourceanalysator_sources;


    public sourceanalysator_Hyperlink(
        String url    ) {
        this.url = url;
        this.sourceanalysator_sources = new ArrayList<>();
    }

    public sourceanalysator_Hyperlink(
        String url        ArrayList<sourceanalysator_Source> sourceanalysator_sources    ) {
        this.url = url;
        this.sourceanalysator_sources = sourceanalysator_sources;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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