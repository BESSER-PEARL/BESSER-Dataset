





import java.util.List;
import java.util.ArrayList;

public class xwiki_HistorySummary extends LinkCollection {

    private String comment;
    private String minorVersion;
    private String modified;
    private String language;
    private String modifier;
    private String wiki;
    private String space;
    private String pageId;
    private String version;
    private String majorVersion;
    private String name;
    private String modifierName;



    public xwiki_HistorySummary(
        String comment,        String minorVersion,        String modified,        String language,        String modifier,        String wiki,        String space,        String pageId,        String version,        String majorVersion,        String name,        String modifierName    ) {
        super(
        );
        this.comment = comment;
        this.minorVersion = minorVersion;
        this.modified = modified;
        this.language = language;
        this.modifier = modifier;
        this.wiki = wiki;
        this.space = space;
        this.pageId = pageId;
        this.version = version;
        this.majorVersion = majorVersion;
        this.name = name;
        this.modifierName = modifierName;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getMinorversion() {
        return minorVersion;
    }

    public void setMinorversion(String minorVersion) {
        this.minorVersion = minorVersion;
    }
    public String getModified() {
        return modified;
    }

    public void setModified(String modified) {
        this.modified = modified;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getWiki() {
        return wiki;
    }

    public void setWiki(String wiki) {
        this.wiki = wiki;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }
    public String getPageid() {
        return pageId;
    }

    public void setPageid(String pageId) {
        this.pageId = pageId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getMajorversion() {
        return majorVersion;
    }

    public void setMajorversion(String majorVersion) {
        this.majorVersion = majorVersion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModifiername() {
        return modifierName;
    }

    public void setModifiername(String modifierName) {
        this.modifierName = modifierName;
    }


}