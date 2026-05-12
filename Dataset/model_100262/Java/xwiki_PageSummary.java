





import java.util.List;
import java.util.ArrayList;

public class xwiki_PageSummary extends LinkCollection {

    private String parent;
    private String parentId;
    private String title;
    private String author;
    private String authorName;
    private String fullName;
    private String id;
    private String xwikiRelativeUrl;
    private String xwikiAbsoluteUrl;
    private String version;
    private String name;
    private String wiki;
    private String syntax;
    private String space;





    private xwiki_PagesType xwiki_pagestype;


    public xwiki_PageSummary(
        String parent,        String parentId,        String title,        String author,        String authorName,        String fullName,        String id,        String xwikiRelativeUrl,        String xwikiAbsoluteUrl,        String version,        String name,        String wiki,        String syntax,        String space    ) {
        super(
        );
        this.parent = parent;
        this.parentId = parentId;
        this.title = title;
        this.author = author;
        this.authorName = authorName;
        this.fullName = fullName;
        this.id = id;
        this.xwikiRelativeUrl = xwikiRelativeUrl;
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
        this.version = version;
        this.name = name;
        this.wiki = wiki;
        this.syntax = syntax;
        this.space = space;
    }


    public String getParent() {
        return parent;
    }

    public void setParent(String parent) {
        this.parent = parent;
    }
    public String getParentid() {
        return parentId;
    }

    public void setParentid(String parentId) {
        this.parentId = parentId;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getXwikirelativeurl() {
        return xwikiRelativeUrl;
    }

    public void setXwikirelativeurl(String xwikiRelativeUrl) {
        this.xwikiRelativeUrl = xwikiRelativeUrl;
    }
    public String getXwikiabsoluteurl() {
        return xwikiAbsoluteUrl;
    }

    public void setXwikiabsoluteurl(String xwikiAbsoluteUrl) {
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWiki() {
        return wiki;
    }

    public void setWiki(String wiki) {
        this.wiki = wiki;
    }
    public String getSyntax() {
        return syntax;
    }

    public void setSyntax(String syntax) {
        this.syntax = syntax;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }

    public xwiki_PagesType getXwiki_pagestype() {
        return xwiki_pagestype;
    }

    public void setXwiki_pagestype(xwiki_PagesType xwiki_pagestype) {
        this.xwiki_pagestype = xwiki_pagestype;
    }

}