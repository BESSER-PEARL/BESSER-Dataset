





import java.util.List;
import java.util.ArrayList;

public class frameweb_IRI extends Property {

    private String iri;
    private String iriVersion;



    public frameweb_IRI(
        String iri,        String iriVersion    ) {
        super(
        );
        this.iri = iri;
        this.iriVersion = iriVersion;
    }


    public String getIri() {
        return iri;
    }

    public void setIri(String iri) {
        this.iri = iri;
    }
    public String getIriversion() {
        return iriVersion;
    }

    public void setIriversion(String iriVersion) {
        this.iriVersion = iriVersion;
    }


}