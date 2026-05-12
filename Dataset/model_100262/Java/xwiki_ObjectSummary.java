





import java.util.List;
import java.util.ArrayList;

public class xwiki_ObjectSummary extends LinkCollection {

    private String number;
    private String id;
    private String pageAuthorName;
    private String guid;
    private String wiki;
    private String pageAuthor;
    private String className;
    private String pageVersion;
    private String pageId;
    private String space;
    private String pageName;
    private String headline;





    private xwiki_ObjectsType xwiki_objectstype;


    public xwiki_ObjectSummary(
        String number,        String id,        String pageAuthorName,        String guid,        String wiki,        String pageAuthor,        String className,        String pageVersion,        String pageId,        String space,        String pageName,        String headline    ) {
        super(
        );
        this.number = number;
        this.id = id;
        this.pageAuthorName = pageAuthorName;
        this.guid = guid;
        this.wiki = wiki;
        this.pageAuthor = pageAuthor;
        this.className = className;
        this.pageVersion = pageVersion;
        this.pageId = pageId;
        this.space = space;
        this.pageName = pageName;
        this.headline = headline;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPageauthorname() {
        return pageAuthorName;
    }

    public void setPageauthorname(String pageAuthorName) {
        this.pageAuthorName = pageAuthorName;
    }
    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public String getWiki() {
        return wiki;
    }

    public void setWiki(String wiki) {
        this.wiki = wiki;
    }
    public String getPageauthor() {
        return pageAuthor;
    }

    public void setPageauthor(String pageAuthor) {
        this.pageAuthor = pageAuthor;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getPageversion() {
        return pageVersion;
    }

    public void setPageversion(String pageVersion) {
        this.pageVersion = pageVersion;
    }
    public String getPageid() {
        return pageId;
    }

    public void setPageid(String pageId) {
        this.pageId = pageId;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }
    public String getPagename() {
        return pageName;
    }

    public void setPagename(String pageName) {
        this.pageName = pageName;
    }
    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }

    public xwiki_ObjectsType getXwiki_objectstype() {
        return xwiki_objectstype;
    }

    public void setXwiki_objectstype(xwiki_ObjectsType xwiki_objectstype) {
        this.xwiki_objectstype = xwiki_objectstype;
    }

}