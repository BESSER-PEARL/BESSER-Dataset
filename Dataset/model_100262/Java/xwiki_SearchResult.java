





import java.util.List;
import java.util.ArrayList;

public class xwiki_SearchResult extends LinkCollection {

    private String type;
    private String className;
    private String pageName;
    private String score;
    private String wiki;
    private String space;
    private String version;
    private String filename;
    private String language;
    private String modified;
    private String author;
    private String id;
    private String pageFullName;
    private String authorName;
    private String title;
    private String objectNumber;



    public xwiki_SearchResult(
        String type,        String className,        String pageName,        String score,        String wiki,        String space,        String version,        String filename,        String language,        String modified,        String author,        String id,        String pageFullName,        String authorName,        String title,        String objectNumber    ) {
        super(
        );
        this.type = type;
        this.className = className;
        this.pageName = pageName;
        this.score = score;
        this.wiki = wiki;
        this.space = space;
        this.version = version;
        this.filename = filename;
        this.language = language;
        this.modified = modified;
        this.author = author;
        this.id = id;
        this.pageFullName = pageFullName;
        this.authorName = authorName;
        this.title = title;
        this.objectNumber = objectNumber;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getPagename() {
        return pageName;
    }

    public void setPagename(String pageName) {
        this.pageName = pageName;
    }
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getModified() {
        return modified;
    }

    public void setModified(String modified) {
        this.modified = modified;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPagefullname() {
        return pageFullName;
    }

    public void setPagefullname(String pageFullName) {
        this.pageFullName = pageFullName;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getObjectnumber() {
        return objectNumber;
    }

    public void setObjectnumber(String objectNumber) {
        this.objectNumber = objectNumber;
    }


}