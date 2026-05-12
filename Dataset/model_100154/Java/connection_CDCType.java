





import java.util.List;
import java.util.ArrayList;

public class connection_CDCType extends AbstractMetadataObject {

    private String journalName;
    private String linkDB;



    public connection_CDCType(
        String journalName,        String linkDB    ) {
        super(
        );
        this.journalName = journalName;
        this.linkDB = linkDB;
    }


    public String getJournalname() {
        return journalName;
    }

    public void setJournalname(String journalName) {
        this.journalName = journalName;
    }
    public String getLinkdb() {
        return linkDB;
    }

    public void setLinkdb(String linkDB) {
        this.linkDB = linkDB;
    }


}