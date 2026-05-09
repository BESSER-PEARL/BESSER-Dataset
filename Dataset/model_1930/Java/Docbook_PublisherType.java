





import java.util.List;
import java.util.ArrayList;

public class Docbook_PublisherType  {

    private String publishername;





    private Docbook_InfoType docbook_infotype;




    private Docbook_DocumentRoot docbook_documentroot;




    private Docbook_AddressType docbook_addresstype;


    public Docbook_PublisherType(
        String publishername    ) {
        this.publishername = publishername;
    }


    public String getPublishername() {
        return publishername;
    }

    public void setPublishername(String publishername) {
        this.publishername = publishername;
    }

    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }
    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public Docbook_AddressType getDocbook_addresstype() {
        return docbook_addresstype;
    }

    public void setDocbook_addresstype(Docbook_AddressType docbook_addresstype) {
        this.docbook_addresstype = docbook_addresstype;
    }

}