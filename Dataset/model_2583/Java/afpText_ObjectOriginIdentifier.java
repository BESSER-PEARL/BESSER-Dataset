





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectOriginIdentifier extends triplet {

    private String System;
    private String DSID;
    private String MedID;
    private String SysID;



    public afpText_ObjectOriginIdentifier(
        String System,        String DSID,        String MedID,        String SysID    ) {
        super(
        );
        this.System = System;
        this.DSID = DSID;
        this.MedID = MedID;
        this.SysID = SysID;
    }


    public String getSystem() {
        return System;
    }

    public void setSystem(String System) {
        this.System = System;
    }
    public String getDsid() {
        return DSID;
    }

    public void setDsid(String DSID) {
        this.DSID = DSID;
    }
    public String getMedid() {
        return MedID;
    }

    public void setMedid(String MedID) {
        this.MedID = MedID;
    }
    public String getSysid() {
        return SysID;
    }

    public void setSysid(String SysID) {
        this.SysID = SysID;
    }


}