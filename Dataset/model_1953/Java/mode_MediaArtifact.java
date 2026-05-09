





import java.util.List;
import java.util.ArrayList;

public class mode_MediaArtifact  {

    private String name;
    private String source;
    private String identifier;





    private mode_MediaCollection mode_mediacollection;




    private mode_MediaCollection mode_mediacollection;


    public mode_MediaArtifact(
        String name,        String source,        String identifier    ) {
        this.name = name;
        this.source = source;
        this.identifier = identifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public mode_MediaCollection getMode_mediacollection() {
        return mode_mediacollection;
    }

    public void setMode_mediacollection(mode_MediaCollection mode_mediacollection) {
        this.mode_mediacollection = mode_mediacollection;
    }
    public mode_MediaCollection getMode_mediacollection() {
        return mode_mediacollection;
    }

    public void setMode_mediacollection(mode_MediaCollection mode_mediacollection) {
        this.mode_mediacollection = mode_mediacollection;
    }

}