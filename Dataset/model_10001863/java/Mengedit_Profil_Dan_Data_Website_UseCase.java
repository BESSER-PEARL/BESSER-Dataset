





import java.util.List;
import java.util.ArrayList;

public class Mengedit_Profil_Dan_Data_Website_UseCase  {






    private Admin_Website_Actor admin_website_actor;




    private Website_Informasi_Tumbuhan_Herbal_UseCase website_informasi_tumbuhan_herbal_usecase;


    public Mengedit_Profil_Dan_Data_Website_UseCase(
    ) {
    }



    public Admin_Website_Actor getAdmin_website_actor() {
        return admin_website_actor;
    }

    public void setAdmin_website_actor(Admin_Website_Actor admin_website_actor) {
        this.admin_website_actor = admin_website_actor;
    }
    public Website_Informasi_Tumbuhan_Herbal_UseCase getWebsite_informasi_tumbuhan_herbal_usecase() {
        return website_informasi_tumbuhan_herbal_usecase;
    }

    public void setWebsite_informasi_tumbuhan_herbal_usecase(Website_Informasi_Tumbuhan_Herbal_UseCase website_informasi_tumbuhan_herbal_usecase) {
        this.website_informasi_tumbuhan_herbal_usecase = website_informasi_tumbuhan_herbal_usecase;
    }

}