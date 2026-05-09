





import java.util.List;
import java.util.ArrayList;

public class Docbook_AuthorType  {

    private String contrib;





    private Docbook_AddressType docbook_addresstype;


    public Docbook_AuthorType(
        String contrib    ) {
        this.contrib = contrib;
    }


    public String getContrib() {
        return contrib;
    }

    public void setContrib(String contrib) {
        this.contrib = contrib;
    }

    public Docbook_AddressType getDocbook_addresstype() {
        return docbook_addresstype;
    }

    public void setDocbook_addresstype(Docbook_AddressType docbook_addresstype) {
        this.docbook_addresstype = docbook_addresstype;
    }

}