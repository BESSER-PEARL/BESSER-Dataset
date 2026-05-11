





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_ReqID  {

    private String name;
    private String reqID;





    private reqLanguage_Requirement reqlanguage_requirement;


    public reqLanguage_ReqID(
        String name,        String reqID    ) {
        this.name = name;
        this.reqID = reqID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReqid() {
        return reqID;
    }

    public void setReqid(String reqID) {
        this.reqID = reqID;
    }

    public reqLanguage_Requirement getReqlanguage_requirement() {
        return reqlanguage_requirement;
    }

    public void setReqlanguage_requirement(reqLanguage_Requirement reqlanguage_requirement) {
        this.reqlanguage_requirement = reqlanguage_requirement;
    }

}