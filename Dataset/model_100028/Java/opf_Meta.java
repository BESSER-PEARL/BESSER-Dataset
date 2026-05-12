





import java.util.List;
import java.util.ArrayList;

public class opf_Meta  {

    private String scheme;
    private String property;
    private String id;
    private String dir;
    private String refines;
    private String name;
    private String content;





    private opf_Metadata opf_metadata;


    public opf_Meta(
        String scheme,        String property,        String id,        String dir,        String refines,        String name,        String content    ) {
        this.scheme = scheme;
        this.property = property;
        this.id = id;
        this.dir = dir;
        this.refines = refines;
        this.name = name;
        this.content = content;
    }


    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getRefines() {
        return refines;
    }

    public void setRefines(String refines) {
        this.refines = refines;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public opf_Metadata getOpf_metadata() {
        return opf_metadata;
    }

    public void setOpf_metadata(opf_Metadata opf_metadata) {
        this.opf_metadata = opf_metadata;
    }

}