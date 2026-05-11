





import java.util.List;
import java.util.ArrayList;

public class application_MashupAdmin  {

    private String isConfigurationAdmin;
    private String id;
    private String email;
    private String provider;
    private String profileImage;
    private String name;
    private String localIdent;





    private List<application_Mashup> application_mashups;




    private application_Mashup application_mashup;


    public application_MashupAdmin(
        String isConfigurationAdmin,        String id,        String email,        String provider,        String profileImage,        String name,        String localIdent    ) {
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.id = id;
        this.email = email;
        this.provider = provider;
        this.profileImage = profileImage;
        this.name = name;
        this.localIdent = localIdent;
        this.application_mashups = new ArrayList<>();
    }

    public application_MashupAdmin(
        String isConfigurationAdmin,        String id,        String email,        String provider,        String profileImage,        String name,        String localIdent        ArrayList<application_Mashup> application_mashups    ) {
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.id = id;
        this.email = email;
        this.provider = provider;
        this.profileImage = profileImage;
        this.name = name;
        this.localIdent = localIdent;
        this.application_mashups = application_mashups;
    }

    public String getIsconfigurationadmin() {
        return isConfigurationAdmin;
    }

    public void setIsconfigurationadmin(String isConfigurationAdmin) {
        this.isConfigurationAdmin = isConfigurationAdmin;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getProfileimage() {
        return profileImage;
    }

    public void setProfileimage(String profileImage) {
        this.profileImage = profileImage;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLocalident() {
        return localIdent;
    }

    public void setLocalident(String localIdent) {
        this.localIdent = localIdent;
    }

    public List<application_Mashup> getApplication_mashups() {
        return application_mashups;
    }

    public void addApplication_mashup(Application_mashup application_mashup) {
        this.application_mashups.add(application_mashup);
    }
    public application_Mashup getApplication_mashup() {
        return application_mashup;
    }

    public void setApplication_mashup(application_Mashup application_mashup) {
        this.application_mashup = application_mashup;
    }

}