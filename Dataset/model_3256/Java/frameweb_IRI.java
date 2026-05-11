





import java.util.List;
import java.util.ArrayList;

public class frameweb_IRI extends Property {

    private String iriVersion;
    private String iri;



    public frameweb_IRI(
        String iriVersion,        String iri    ) {
        super(
        );
        this.iriVersion = iriVersion;
        this.iri = iri;
    }


    public String getIriversion() {
        return iriVersion;
    }

    public void setIriversion(String iriVersion) {
        this.iriVersion = iriVersion;
    }
    public String getIri() {
        return iri;
    }

    public void setIri(String iri) {
        this.iri = iri;
    }


}