





import java.util.List;
import java.util.ArrayList;

public class Medeina  {

    private None blackList_User_;
    private String attribute;



    public Medeina(
        None blackList_User_,        String attribute    ) {
        this.blackList_User_ = blackList_User_;
        this.attribute = attribute;
    }


    public None getBlacklist_user_() {
        return blackList_User_;
    }

    public void setBlacklist_user_(None blackList_User_) {
        this.blackList_User_ = blackList_User_;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}