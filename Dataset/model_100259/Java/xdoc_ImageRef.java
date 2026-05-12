





import java.util.List;
import java.util.ArrayList;

public class xdoc_ImageRef extends MarkUp {

    private String name;
    private String style;
    private String caption;
    private String path;
    private String clazz;



    public xdoc_ImageRef(
        String name,        String style,        String caption,        String path,        String clazz    ) {
        super(
        );
        this.name = name;
        this.style = style;
        this.caption = caption;
        this.path = path;
        this.clazz = clazz;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getCaption() {
        return caption;
    }

    public void setCaption(String caption) {
        this.caption = caption;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getClazz() {
        return clazz;
    }

    public void setClazz(String clazz) {
        this.clazz = clazz;
    }


}