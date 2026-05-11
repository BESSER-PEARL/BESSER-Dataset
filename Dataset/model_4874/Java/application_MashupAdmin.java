





import java.util.List;
import java.util.ArrayList;

public class application_MashupAdmin  {

    private String email;
    private String localIdent;
    private String isConfigurationAdmin;
    private String profileImage;
    private String provider;
    private String name;
    private String id;





    private application_Mashup application_mashup;




    private List<application_Mashup> application_mashups;


    public application_MashupAdmin(
        String email,        String localIdent,        String isConfigurationAdmin,        String profileImage,        String provider,        String name,        String id    ) {
        this.email = email;
        this.localIdent = localIdent;
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.profileImage = profileImage;
        this.provider = provider;
        this.name = name;
        this.id = id;
        this.application_mashups = new ArrayList<>();
    }

    public application_MashupAdmin(
        String email,        String localIdent,        String isConfigurationAdmin,        String profileImage,        String provider,        String name,        String id        ArrayList<application_Mashup> application_mashups    ) {
        this.email = email;
        this.localIdent = localIdent;
        this.isConfigurationAdmin = isConfigurationAdmin;
        this.profileImage = profileImage;
        this.provider = provider;
        this.name = name;
        this.id = id;
        this.application_mashups = application_mashups;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLocalident() {
        return localIdent;
    }

    public void setLocalident(String localIdent) {
        this.localIdent = localIdent;
    }
    public String getIsconfigurationadmin() {
        return isConfigurationAdmin;
    }

    public void setIsconfigurationadmin(String isConfigurationAdmin) {
        this.isConfigurationAdmin = isConfigurationAdmin;
    }
    public String getProfileimage() {
        return profileImage;
    }

    public void setProfileimage(String profileImage) {
        this.profileImage = profileImage;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public application_Mashup getApplication_mashup() {
        return application_mashup;
    }

    public void setApplication_mashup(application_Mashup application_mashup) {
        this.application_mashup = application_mashup;
    }
    public List<application_Mashup> getApplication_mashups() {
        return application_mashups;
    }

    public void addApplication_mashup(Application_mashup application_mashup) {
        this.application_mashups.add(application_mashup);
    }

}