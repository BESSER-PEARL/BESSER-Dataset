





import java.util.List;
import java.util.ArrayList;

public class idl_StateMember  {

    private boolean isPublic;
    private String names;





    private idl_ParamTypeSpec idl_paramtypespec;




    private idl_EventDcl idl_eventdcl;


    public idl_StateMember(
        boolean isPublic,        String names    ) {
        this.isPublic = isPublic;
        this.names = names;
    }


    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }
    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public idl_ParamTypeSpec getIdl_paramtypespec() {
        return idl_paramtypespec;
    }

    public void setIdl_paramtypespec(idl_ParamTypeSpec idl_paramtypespec) {
        this.idl_paramtypespec = idl_paramtypespec;
    }
    public idl_EventDcl getIdl_eventdcl() {
        return idl_eventdcl;
    }

    public void setIdl_eventdcl(idl_EventDcl idl_eventdcl) {
        this.idl_eventdcl = idl_eventdcl;
    }

}