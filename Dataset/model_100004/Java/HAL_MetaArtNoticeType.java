





import java.util.List;
import java.util.ArrayList;

public class HAL_MetaArtNoticeType extends MetaType {

    private String domain;
    private String abstract;





    private ReferenceBiblioType referencebibliotype;


    public HAL_MetaArtNoticeType(
        String domain,        String abstract    ) {
        super(
        );
        this.domain = domain;
        this.abstract = abstract;
    }


    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public ReferenceBiblioType getReferencebibliotype() {
        return referencebibliotype;
    }

    public void setReferencebibliotype(ReferenceBiblioType referencebibliotype) {
        this.referencebibliotype = referencebibliotype;
    }

}