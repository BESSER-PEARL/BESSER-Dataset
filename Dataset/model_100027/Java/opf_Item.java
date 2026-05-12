





import java.util.List;
import java.util.ArrayList;

public class opf_Item  {

    private boolean noToc;
    private String required_namespace;
    private String sourcePath;
    private boolean generated;
    private String href;
    private String fallback;
    private String file;
    private String title;
    private String fallback_style;
    private String id;
    private String media_type;
    private String required_modules;



    public opf_Item(
        boolean noToc,        String required_namespace,        String sourcePath,        boolean generated,        String href,        String fallback,        String file,        String title,        String fallback_style,        String id,        String media_type,        String required_modules    ) {
        this.noToc = noToc;
        this.required_namespace = required_namespace;
        this.sourcePath = sourcePath;
        this.generated = generated;
        this.href = href;
        this.fallback = fallback;
        this.file = file;
        this.title = title;
        this.fallback_style = fallback_style;
        this.id = id;
        this.media_type = media_type;
        this.required_modules = required_modules;
    }


    public boolean getNotoc() {
        return noToc;
    }

    public void setNotoc(boolean noToc) {
        this.noToc = noToc;
    }
    public String getRequired_namespace() {
        return required_namespace;
    }

    public void setRequired_namespace(String required_namespace) {
        this.required_namespace = required_namespace;
    }
    public String getSourcepath() {
        return sourcePath;
    }

    public void setSourcepath(String sourcePath) {
        this.sourcePath = sourcePath;
    }
    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getFallback() {
        return fallback;
    }

    public void setFallback(String fallback) {
        this.fallback = fallback;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getFallback_style() {
        return fallback_style;
    }

    public void setFallback_style(String fallback_style) {
        this.fallback_style = fallback_style;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMedia_type() {
        return media_type;
    }

    public void setMedia_type(String media_type) {
        this.media_type = media_type;
    }
    public String getRequired_modules() {
        return required_modules;
    }

    public void setRequired_modules(String required_modules) {
        this.required_modules = required_modules;
    }


}