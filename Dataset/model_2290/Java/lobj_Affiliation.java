





import java.util.List;
import java.util.ArrayList;

public class lobj_Affiliation  {

    private String orgdiv;
    private String jobtitle;
    private String id;
    private String orgname;
    private String shortaffil;



    public lobj_Affiliation(
        String orgdiv,        String jobtitle,        String id,        String orgname,        String shortaffil    ) {
        this.orgdiv = orgdiv;
        this.jobtitle = jobtitle;
        this.id = id;
        this.orgname = orgname;
        this.shortaffil = shortaffil;
    }


    public String getOrgdiv() {
        return orgdiv;
    }

    public void setOrgdiv(String orgdiv) {
        this.orgdiv = orgdiv;
    }
    public String getJobtitle() {
        return jobtitle;
    }

    public void setJobtitle(String jobtitle) {
        this.jobtitle = jobtitle;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getOrgname() {
        return orgname;
    }

    public void setOrgname(String orgname) {
        this.orgname = orgname;
    }
    public String getShortaffil() {
        return shortaffil;
    }

    public void setShortaffil(String shortaffil) {
        this.shortaffil = shortaffil;
    }


}