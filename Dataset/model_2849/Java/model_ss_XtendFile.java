





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendFile  {

    private String package;





    private XExportSection xexportsection;




    private XImportSection1 ximportsection1;


    public model_ss_XtendFile(
        String package    ) {
        this.package = package;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public XExportSection getXexportsection() {
        return xexportsection;
    }

    public void setXexportsection(XExportSection xexportsection) {
        this.xexportsection = xexportsection;
    }
    public XImportSection1 getXimportsection1() {
        return ximportsection1;
    }

    public void setXimportsection1(XImportSection1 ximportsection1) {
        this.ximportsection1 = ximportsection1;
    }

}