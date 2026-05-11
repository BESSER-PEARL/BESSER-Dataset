





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ResponsiblesType  {

    private String responsible;





    private xpdl1_RedefinableHeaderType xpdl1_redefinableheadertype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_ResponsiblesType(
        String responsible    ) {
        this.responsible = responsible;
    }


    public String getResponsible() {
        return responsible;
    }

    public void setResponsible(String responsible) {
        this.responsible = responsible;
    }

    public xpdl1_RedefinableHeaderType getXpdl1_redefinableheadertype() {
        return xpdl1_redefinableheadertype;
    }

    public void setXpdl1_redefinableheadertype(xpdl1_RedefinableHeaderType xpdl1_redefinableheadertype) {
        this.xpdl1_redefinableheadertype = xpdl1_redefinableheadertype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}