





import java.util.List;
import java.util.ArrayList;

public class eol_EOLElement  {

    private String uri;





    private eol_EOLElement eol_eolelement;


    public eol_EOLElement(
        String uri    ) {
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public eol_EOLElement getEol_eolelement() {
        return eol_eolelement;
    }

    public void setEol_eolelement(eol_EOLElement eol_eolelement) {
        this.eol_eolelement = eol_eolelement;
    }

}