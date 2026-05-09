





import java.util.List;
import java.util.ArrayList;

public class iTrace_Artefact  {

    private String path;
    private String aspect;
    private String name;
    private String abstractionLevel;



    public iTrace_Artefact(
        String path,        String aspect,        String name,        String abstractionLevel    ) {
        this.path = path;
        this.aspect = aspect;
        this.name = name;
        this.abstractionLevel = abstractionLevel;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getAspect() {
        return aspect;
    }

    public void setAspect(String aspect) {
        this.aspect = aspect;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbstractionlevel() {
        return abstractionLevel;
    }

    public void setAbstractionlevel(String abstractionLevel) {
        this.abstractionLevel = abstractionLevel;
    }


}