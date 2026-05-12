





import java.util.List;
import java.util.ArrayList;

public class connection_CDCType extends AbstractMetadataObject {

    private String linkDB;
    private String journalName;



    public connection_CDCType(
        String linkDB,        String journalName    ) {
        super(
        );
        this.linkDB = linkDB;
        this.journalName = journalName;
    }


    public String getLinkdb() {
        return linkDB;
    }

    public void setLinkdb(String linkDB) {
        this.linkDB = linkDB;
    }
    public String getJournalname() {
        return journalName;
    }

    public void setJournalname(String journalName) {
        this.journalName = journalName;
    }


}