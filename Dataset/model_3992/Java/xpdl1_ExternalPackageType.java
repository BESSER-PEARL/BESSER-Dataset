





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ExternalPackageType  {

    private String href;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;


    public xpdl1_ExternalPackageType(
        String href    ) {
        this.href = href;
    }


    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }

}