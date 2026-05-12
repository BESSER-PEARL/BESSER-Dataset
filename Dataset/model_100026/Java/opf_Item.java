





import java.util.List;
import java.util.ArrayList;

public class opf_Item  {

    private String id;
    private boolean noToc;
    private String href;
    private String sourcePath;
    private String title;
    private String file;
    private String fallback_style;
    private boolean generated;
    private String fallback;
    private String media_type;
    private String required_namespace;
    private String required_modules;





    private opf_Manifest opf_manifest;


    public opf_Item(
        String id,        boolean noToc,        String href,        String sourcePath,        String title,        String file,        String fallback_style,        boolean generated,        String fallback,        String media_type,        String required_namespace,        String required_modules    ) {
        this.id = id;
        this.noToc = noToc;
        this.href = href;
        this.sourcePath = sourcePath;
        this.title = title;
        this.file = file;
        this.fallback_style = fallback_style;
        this.generated = generated;
        this.fallback = fallback;
        this.media_type = media_type;
        this.required_namespace = required_namespace;
        this.required_modules = required_modules;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getNotoc() {
        return noToc;
    }

    public void setNotoc(boolean noToc) {
        this.noToc = noToc;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getSourcepath() {
        return sourcePath;
    }

    public void setSourcepath(String sourcePath) {
        this.sourcePath = sourcePath;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getFallback_style() {
        return fallback_style;
    }

    public void setFallback_style(String fallback_style) {
        this.fallback_style = fallback_style;
    }
    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }
    public String getFallback() {
        return fallback;
    }

    public void setFallback(String fallback) {
        this.fallback = fallback;
    }
    public String getMedia_type() {
        return media_type;
    }

    public void setMedia_type(String media_type) {
        this.media_type = media_type;
    }
    public String getRequired_namespace() {
        return required_namespace;
    }

    public void setRequired_namespace(String required_namespace) {
        this.required_namespace = required_namespace;
    }
    public String getRequired_modules() {
        return required_modules;
    }

    public void setRequired_modules(String required_modules) {
        this.required_modules = required_modules;
    }

    public opf_Manifest getOpf_manifest() {
        return opf_manifest;
    }

    public void setOpf_manifest(opf_Manifest opf_manifest) {
        this.opf_manifest = opf_manifest;
    }

}