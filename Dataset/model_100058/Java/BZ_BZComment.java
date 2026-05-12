




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class BZ_BZComment  {

    private String commentId;
    private int issueId;
    private String commentAuthor;
    private String commentText;
    private LocalDate commentTime;
    private String commentHTML;





    private BZ_BZIssue bz_bzissue;




    private BZ_BZIssue bz_bzissue;


    public BZ_BZComment(
        String commentId,        int issueId,        String commentAuthor,        String commentText,        LocalDate commentTime,        String commentHTML    ) {
        this.commentId = commentId;
        this.issueId = issueId;
        this.commentAuthor = commentAuthor;
        this.commentText = commentText;
        this.commentTime = commentTime;
        this.commentHTML = commentHTML;
    }


    public String getCommentid() {
        return commentId;
    }

    public void setCommentid(String commentId) {
        this.commentId = commentId;
    }
    public int getIssueid() {
        return issueId;
    }

    public void setIssueid(int issueId) {
        this.issueId = issueId;
    }
    public String getCommentauthor() {
        return commentAuthor;
    }

    public void setCommentauthor(String commentAuthor) {
        this.commentAuthor = commentAuthor;
    }
    public String getCommenttext() {
        return commentText;
    }

    public void setCommenttext(String commentText) {
        this.commentText = commentText;
    }
    public LocalDate getCommenttime() {
        return commentTime;
    }

    public void setCommenttime(LocalDate commentTime) {
        this.commentTime = commentTime;
    }
    public String getCommenthtml() {
        return commentHTML;
    }

    public void setCommenthtml(String commentHTML) {
        this.commentHTML = commentHTML;
    }

    public BZ_BZIssue getBz_bzissue() {
        return bz_bzissue;
    }

    public void setBz_bzissue(BZ_BZIssue bz_bzissue) {
        this.bz_bzissue = bz_bzissue;
    }
    public BZ_BZIssue getBz_bzissue() {
        return bz_bzissue;
    }

    public void setBz_bzissue(BZ_BZIssue bz_bzissue) {
        this.bz_bzissue = bz_bzissue;
    }

}