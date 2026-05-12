





import java.util.List;
import java.util.ArrayList;

public class xwiki_AttachmentsType extends LinkCollection {






    private List<xwiki_Attachment> xwiki_attachments;


    public xwiki_AttachmentsType(
    ) {
        super(
        );
        this.xwiki_attachments = new ArrayList<>();
    }

    public xwiki_AttachmentsType(
        ArrayList<xwiki_Attachment> xwiki_attachments    ) {
        this.xwiki_attachments = xwiki_attachments;
    }


    public List<xwiki_Attachment> getXwiki_attachments() {
        return xwiki_attachments;
    }

    public void addXwiki_attachment(Xwiki_attachment xwiki_attachment) {
        this.xwiki_attachments.add(xwiki_attachment);
    }

}