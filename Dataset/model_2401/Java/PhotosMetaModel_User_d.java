





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_User_d extends Entities {

    private String username;
    private String first_name;
    private String profile_description;
    private String password;
    private String email;
    private String last_name;





    private PhotosMetaModel_Functionalities photosmetamodel_functionalities;


    public PhotosMetaModel_User_d(
        String username,        String first_name,        String profile_description,        String password,        String email,        String last_name    ) {
        super(
        );
        this.username = username;
        this.first_name = first_name;
        this.profile_description = profile_description;
        this.password = password;
        this.email = email;
        this.last_name = last_name;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public String getProfile_description() {
        return profile_description;
    }

    public void setProfile_description(String profile_description) {
        this.profile_description = profile_description;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public PhotosMetaModel_Functionalities getPhotosmetamodel_functionalities() {
        return photosmetamodel_functionalities;
    }

    public void setPhotosmetamodel_functionalities(PhotosMetaModel_Functionalities photosmetamodel_functionalities) {
        this.photosmetamodel_functionalities = photosmetamodel_functionalities;
    }

}