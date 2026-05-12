





import java.util.List;
import java.util.ArrayList;

public class orgnazition  {

    private String orgID;
    private String establishedDate;
    private String icon;
    private String name;
    private None president;



    public orgnazition(
        String orgID,        String establishedDate,        String icon,        String name,        None president    ) {
        this.orgID = orgID;
        this.establishedDate = establishedDate;
        this.icon = icon;
        this.name = name;
        this.president = president;
    }


    public String getOrgid() {
        return orgID;
    }

    public void setOrgid(String orgID) {
        this.orgID = orgID;
    }
    public String getEstablisheddate() {
        return establishedDate;
    }

    public void setEstablisheddate(String establishedDate) {
        this.establishedDate = establishedDate;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getPresident() {
        return president;
    }

    public void setPresident(None president) {
        this.president = president;
    }


}