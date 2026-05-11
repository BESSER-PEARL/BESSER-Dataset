





import java.util.List;
import java.util.ArrayList;

public class moba_MobaDtoAttribute extends MobaDtoFeature, MobaConstraintable, MobaMultiplicityAble {

    private boolean domainKey;
    private String alias;
    private String formatString;
    private boolean lazy;
    private boolean domainDescription;
    private boolean transient;





    private moba_MobaDataType moba_mobadatatype;


    public moba_MobaDtoAttribute(
        boolean domainKey,        String alias,        String formatString,        boolean lazy,        boolean domainDescription,        boolean transient    ) {
        super(
        );
        this.domainKey = domainKey;
        this.alias = alias;
        this.formatString = formatString;
        this.lazy = lazy;
        this.domainDescription = domainDescription;
        this.transient = transient;
    }


    public boolean getDomainkey() {
        return domainKey;
    }

    public void setDomainkey(boolean domainKey) {
        this.domainKey = domainKey;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getFormatstring() {
        return formatString;
    }

    public void setFormatstring(String formatString) {
        this.formatString = formatString;
    }
    public boolean getLazy() {
        return lazy;
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public boolean getDomaindescription() {
        return domainDescription;
    }

    public void setDomaindescription(boolean domainDescription) {
        this.domainDescription = domainDescription;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public moba_MobaDataType getMoba_mobadatatype() {
        return moba_mobadatatype;
    }

    public void setMoba_mobadatatype(moba_MobaDataType moba_mobadatatype) {
        this.moba_mobadatatype = moba_mobadatatype;
    }

}