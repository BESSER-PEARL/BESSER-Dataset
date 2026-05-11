





import java.util.List;
import java.util.ArrayList;

public class application_MashupAdmin  {

    private String email;
    private String isConfigurationAdmin;
    private String provider;
    private String localIdent;
    private String id;
    private String name;
    private String profileImage;



    public application_MashupAdmin(
        String email,        String isConfigurationAdmin,        String provider,        String localIdent,        String id,        String name,        String profileImage    ) {
        this.email = email;
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.provider = provider;
        this.localIdent = localIdent;
        this.id = id;
        this.name = name;
        this.profileImage = profileImage;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getIsconfigurationadmin() {
        return isConfigurationAdmin;
    }

    public void setIsconfigurationadmin(String isConfigurationAdmin) {
        this.isConfigurationAdmin = isConfigurationAdmin;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getLocalident() {
        return localIdent;
    }

    public void setLocalident(String localIdent) {
        this.localIdent = localIdent;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProfileimage() {
        return profileImage;
    }

    public void setProfileimage(String profileImage) {
        this.profileImage = profileImage;
    }


}