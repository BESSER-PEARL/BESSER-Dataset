





import java.util.List;
import java.util.ArrayList;

public class xwiki_Attachment extends LinkCollection {

    private String mimeType;
    private String authorName;
    private String size;
    private String xwikiAbsoluteUrl;
    private String pageVersion;
    private String name;
    private String date;
    private String author;
    private String version;
    private String pageId;
    private String xwikiRelativeUrl;
    private String id;



    public xwiki_Attachment(
        String mimeType,        String authorName,        String size,        String xwikiAbsoluteUrl,        String pageVersion,        String name,        String date,        String author,        String version,        String pageId,        String xwikiRelativeUrl,        String id    ) {
        super(
        );
        this.mimeType = mimeType;
        this.authorName = authorName;
        this.size = size;
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
        this.pageVersion = pageVersion;
        this.name = name;
        this.date = date;
        this.author = author;
        this.version = version;
        this.pageId = pageId;
        this.xwikiRelativeUrl = xwikiRelativeUrl;
        this.id = id;
    }


    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getXwikiabsoluteurl() {
        return xwikiAbsoluteUrl;
    }

    public void setXwikiabsoluteurl(String xwikiAbsoluteUrl) {
        this.xwikiAbsoluteUrl = xwikiAbsoluteUrl;
    }
    public String getPageversion() {
        return pageVersion;
    }

    public void setPageversion(String pageVersion) {
        this.pageVersion = pageVersion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getPageid() {
        return pageId;
    }

    public void setPageid(String pageId) {
        this.pageId = pageId;
    }
    public String getXwikirelativeurl() {
        return xwikiRelativeUrl;
    }

    public void setXwikirelativeurl(String xwikiRelativeUrl) {
        this.xwikiRelativeUrl = xwikiRelativeUrl;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}