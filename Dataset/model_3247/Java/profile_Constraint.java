





import java.util.List;
import java.util.ArrayList;

public class profile_Constraint  {

    private String type;
    private String operation;
    private int bound;
    private boolean isDerivation;





    private profile_Resource profile_resource;




    private profile_PlatformProfile profile_platformprofile;




    private profile_PlatformProfile profile_platformprofile;


    public profile_Constraint(
        String type,        String operation,        int bound,        boolean isDerivation    ) {
        this.type = type;
        this.operation = operation;
        this.bound = bound;
        this.isDerivation = isDerivation;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }
    public int getBound() {
        return bound;
    }

    public void setBound(int bound) {
        this.bound = bound;
    }
    public boolean getIsderivation() {
        return isDerivation;
    }

    public void setIsderivation(boolean isDerivation) {
        this.isDerivation = isDerivation;
    }

    public profile_Resource getProfile_resource() {
        return profile_resource;
    }

    public void setProfile_resource(profile_Resource profile_resource) {
        this.profile_resource = profile_resource;
    }
    public profile_PlatformProfile getProfile_platformprofile() {
        return profile_platformprofile;
    }

    public void setProfile_platformprofile(profile_PlatformProfile profile_platformprofile) {
        this.profile_platformprofile = profile_platformprofile;
    }
    public profile_PlatformProfile getProfile_platformprofile() {
        return profile_platformprofile;
    }

    public void setProfile_platformprofile(profile_PlatformProfile profile_platformprofile) {
        this.profile_platformprofile = profile_platformprofile;
    }

}