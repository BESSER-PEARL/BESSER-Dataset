





import java.util.List;
import java.util.ArrayList;

public class xwiki_Comment extends LinkCollection {

    private String replyTo;
    private String text;
    private String author;
    private String highlight;
    private String authorName;
    private String id;
    private String pageId;
    private String date;





    private xwiki_CommentsType xwiki_commentstype;


    public xwiki_Comment(
        String replyTo,        String text,        String author,        String highlight,        String authorName,        String id,        String pageId,        String date    ) {
        super(
        );
        this.replyTo = replyTo;
        this.text = text;
        this.author = author;
        this.highlight = highlight;
        this.authorName = authorName;
        this.id = id;
        this.pageId = pageId;
        this.date = date;
    }


    public String getReplyto() {
        return replyTo;
    }

    public void setReplyto(String replyTo) {
        this.replyTo = replyTo;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getHighlight() {
        return highlight;
    }

    public void setHighlight(String highlight) {
        this.highlight = highlight;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPageid() {
        return pageId;
    }

    public void setPageid(String pageId) {
        this.pageId = pageId;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public xwiki_CommentsType getXwiki_commentstype() {
        return xwiki_commentstype;
    }

    public void setXwiki_commentstype(xwiki_CommentsType xwiki_commentstype) {
        this.xwiki_commentstype = xwiki_commentstype;
    }

}