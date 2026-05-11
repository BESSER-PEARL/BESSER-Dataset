





import java.util.List;
import java.util.ArrayList;

public class moba_MobaSettingsAttribute extends MobaSettingsFeature, MobaConstraintable, MobaMultiplicityAble {

    private boolean transient;
    private boolean domainDescription;
    private boolean lazy;
    private boolean domainKey;
    private String formatString;





    private moba_MobaDataType moba_mobadatatype;


    public moba_MobaSettingsAttribute(
        boolean transient,        boolean domainDescription,        boolean lazy,        boolean domainKey,        String formatString    ) {
        super(
        );
        this.transient = transient;
        this.domainDescription = domainDescription;
        this.lazy = lazy;
        this.domainKey = domainKey;
        this.formatString = formatString;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getDomaindescription() {
        return domainDescription;
    }

    public void setDomaindescription(boolean domainDescription) {
        this.domainDescription = domainDescription;
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