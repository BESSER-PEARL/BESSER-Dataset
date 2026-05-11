





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEntityAttribute extends MobaEntityFeature, MobaConstraintable, MobaMultiplicityAble {

    private boolean transient;
    private boolean lazy;
    private boolean domainKey;
    private boolean domainDescription;
    private String formatString;





    private moba_MobaDataType moba_mobadatatype;


    public moba_MobaEntityAttribute(
        boolean transient,        boolean lazy,        boolean domainKey,        boolean domainDescription,        String formatString    ) {
        super(
        );
        this.transient = transient;
        this.lazy = lazy;
        this.domainKey = domainKey;
        this.domainDescription = domainDescription;
        this.formatString = formatString;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getLazy() {
        return lazy;
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public boolean getDomainkey() {
        return domainKey;
    }

    public void setDomainkey(boolean domainKey) {
        this.domainKey = domainKey;
    }
    public boolean getDomaindescription() {
        return domainDescription;
    }

    public void setDomaindescription(boolean domainDescription) {
        this.domainDescription = domainDescription;
    }
    public String getFormatstring() {
        return formatString;
    }

    public void setFormatstring(String formatString) {
        this.formatString = formatString;
    }

    public moba_MobaDataType getMoba_mobadatatype() {
        return moba_mobadatatype;
    }

    public void setMoba_mobadatatype(moba_MobaDataType moba_mobadatatype) {
        this.moba_mobadatatype = moba_mobadatatype;
    }

}