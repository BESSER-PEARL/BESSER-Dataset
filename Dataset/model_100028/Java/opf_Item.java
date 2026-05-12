





import java.util.List;
import java.util.ArrayList;

public class opf_Item  {

    private String sourcePath;
    private String properties;
    private String fallback;
    private String fallback_style;
    private String href;
    private String required_namespace;
    private boolean generated;
    private String media_type;
    private boolean noToc;
    private String required_modules;
    private String id;
    private String media_overlay;
    private String file;
    private String title;





    private opf_Manifest opf_manifest;


    public opf_Item(
        String sourcePath,        String properties,        String fallback,        String fallback_style,        String href,        String required_namespace,        boolean generated,        String media_type,        boolean noToc,        String required_modules,        String id,        String media_overlay,        String file,        String title    ) {
        this.sourcePath = sourcePath;
        this.properties = properties;
        this.fallback = fallback;
        this.fallback_style = fallback_style;
        this.href = href;
        this.required_namespace = required_namespace;
        this.generated = generated;
        this.media_type = media_type;
        this.noToc = noToc;
        this.required_modules = required_modules;
        this.id = id;
        this.media_overlay = media_overlay;
        this.file = file;
        this.title = title;
    }


    public String getSourcepath() {
        return sourcePath;
    }

    public void setSourcepath(String sourcePath) {
        this.sourcePath = sourcePath;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getFallback() {
        return fallback;
    }

    public void setFallback(String fallback) {
        this.fallback = fallback;
    }
    public String getFallback_style() {
        return fallback_style;
    }

    public void setFallback_style(String fallback_style) {
        this.fallback_style = fallback_style;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getRequired_namespace() {
        return required_namespace;
    }

    public void setRequired_namespace(String required_namespace) {
        this.required_namespace = required_namespace;
    }
    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }
    public String getMedia_type() {
        return media_type;
    }

    public void setMedia_type(String media_type) {
        this.media_type = media_type;
    }
    public boolean getNotoc() {
        return noToc;
    }

    public void setNotoc(boolean noToc) {
        this.noToc = noToc;
    }
    public String getRequired_modules() {
        return required_modules;
    }

    public void setRequired_modules(String required_modules) {
        this.required_modules = required_modules;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMedia_overlay() {
        return media_overlay;
    }

    public void setMedia_overlay(String media_overlay) {
        this.media_overlay = media_overlay;
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

    public opf_Manifest getOpf_manifest() {
        return opf_manifest;
    }

    public void setOpf_manifest(opf_Manifest opf_manifest) {
        this.opf_manifest = opf_manifest;
    }

}