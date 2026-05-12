





import java.util.List;
import java.util.ArrayList;

public class XHTML_Param extends ObjectElement, EMPTY {

    private String valuetype;





    private CDATA cdata;




    private CDATA cdata;




    private ContentType contenttype;




    private ID id;


    public XHTML_Param(
        String valuetype    ) {
        super(
        );
        this.valuetype = valuetype;
    }


    public String getValuetype() {
        return valuetype;
    }

    public void setValuetype(String valuetype) {
        this.valuetype = valuetype;
    }

    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
    }
    public ID getId() {
        return id;
    }

    public void setId(ID id) {
        this.id = id;
    }

}