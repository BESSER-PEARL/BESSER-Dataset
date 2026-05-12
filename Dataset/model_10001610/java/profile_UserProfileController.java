





import java.util.List;
import java.util.ArrayList;

public class profile_UserProfileController  {

    private String attribute;
    private None userProfileRepository;
    private String URL;
    private None userAccountRepository;



    public profile_UserProfileController(
        String attribute,        None userProfileRepository,        String URL,        None userAccountRepository    ) {
        this.attribute = attribute;
        this.userProfileRepository = userProfileRepository;
        this.URL = URL;
        this.userAccountRepository = userAccountRepository;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getUserprofilerepository() {
        return userProfileRepository;
    }

    public void setUserprofilerepository(None userProfileRepository) {
        this.userProfileRepository = userProfileRepository;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public None getUseraccountrepository() {
        return userAccountRepository;
    }

    public void setUseraccountrepository(None userAccountRepository) {
        this.userAccountRepository = userAccountRepository;
    }


}