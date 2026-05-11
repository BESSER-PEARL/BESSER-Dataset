





import java.util.List;
import java.util.ArrayList;

public class profile_Resource  {

    private String name;
    private String type;
    private int weight;





    private profile_PlatformProfile profile_platformprofile;


    public profile_Resource(
        String name,        String type,        int weight    ) {
        this.name = name;
        this.type = type;
        this.weight = weight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public profile_PlatformProfile getProfile_platformprofile() {
        return profile_platformprofile;
    }

    public void setProfile_platformprofile(profile_PlatformProfile profile_platformprofile) {
        this.profile_platformprofile = profile_platformprofile;
    }

}