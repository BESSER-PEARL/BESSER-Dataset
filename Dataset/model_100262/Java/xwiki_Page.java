





import java.util.List;
import java.util.ArrayList;

public class xwiki_Page extends PageSummary {

    private String comment;
    private String created;
    private String language;
    private String majorVersion;
    private String modifier;
    private String creatorName;
    private String modified;
    private String minorVersion;
    private String creator;
    private String content;
    private String modifierName;





    private xwiki_DocumentRoot xwiki_documentroot;


    public xwiki_Page(
        String comment,        String created,        String language,        String majorVersion,        String modifier,        String creatorName,        String modified,        String minorVersion,        String creator,        String content,        String modifierName    ) {
        super(
        );
        this.comment = comment;
        this.created = created;
        this.language = language;
        this.majorVersion = majorVersion;
        this.modifier = modifier;
        this.creatorName = creatorName;
        this.modified = modified;
        this.minorVersion = minorVersion;
        this.creator = creator;
        this.content = content;
        this.modifierName = modifierName;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getMajorversion() {
        return majorVersion;
    }

    public void setMajorversion(String majorVersion) {
        this.majorVersion = majorVersion;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getCreatorname() {
        return creatorName;
    }

    public void setCreatorname(String creatorName) {
        this.creatorName = creatorName;
    }
    public String getModified() {
        return modified;
    }

    public void setModified(String modified) {
        this.modified = modified;
    }
    public String getMinorversion() {
        return minorVersion;
    }

    public void setMinorversion(String minorVersion) {
        this.minorVersion = minorVersion;
    }
    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getModifiername() {
        return modifierName;
    }

    public void setModifiername(String modifierName) {
        this.modifierName = modifierName;
    }

    public xwiki_DocumentRoot getXwiki_documentroot() {
        return xwiki_documentroot;
    }

    public void setXwiki_documentroot(xwiki_DocumentRoot xwiki_documentroot) {
        this.xwiki_documentroot = xwiki_documentroot;
    }

}