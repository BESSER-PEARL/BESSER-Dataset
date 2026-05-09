





import java.util.List;
import java.util.ArrayList;

public class Docbook_RefEntryType  {

    private String version;





    private Docbook_ReferenceType docbook_referencetype;




    private Docbook_InfoType docbook_infotype;


    public Docbook_RefEntryType(
        String version    ) {
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public Docbook_ReferenceType getDocbook_referencetype() {
        return docbook_referencetype;
    }

    public void setDocbook_referencetype(Docbook_ReferenceType docbook_referencetype) {
        this.docbook_referencetype = docbook_referencetype;
    }
    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }

}