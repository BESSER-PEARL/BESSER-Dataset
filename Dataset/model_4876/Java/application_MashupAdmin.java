





import java.util.List;
import java.util.ArrayList;

public class application_MashupAdmin  {

    private String name;
    private String profileImage;
    private String localIdent;
    private String email;
    private String id;
    private String isConfigurationAdmin;
    private String provider;



    public application_MashupAdmin(
        String name,        String profileImage,        String localIdent,        String email,        String id,        String isConfigurationAdmin,        String provider    ) {
        this.name = name;
        this.profileImage = profileImage;
        this.localIdent = localIdent;
        this.email = email;
        this.id = id;
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.provider = provider;
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
    public String getLocalident() {
        return localIdent;
    }

    public void setLocalident(String localIdent) {
        this.localIdent = localIdent;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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


}