





import java.util.List;
import java.util.ArrayList;

public class Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase  {






    private Fitur_Fitur_Pada_Website_UseCase fitur_fitur_pada_website_usecase;




    private Admin_Website_Actor admin_website_actor;


    public Fitur_Website_Yang_Dapat_Diakses_Dan_Edit_Oleh_admin_UseCase(
    ) {
    }



    public Fitur_Fitur_Pada_Website_UseCase getFitur_fitur_pada_website_usecase() {
        return fitur_fitur_pada_website_usecase;
    }

    public void setFitur_fitur_pada_website_usecase(Fitur_Fitur_Pada_Website_UseCase fitur_fitur_pada_website_usecase) {
        this.fitur_fitur_pada_website_usecase = fitur_fitur_pada_website_usecase;
    }
    public Admin_Website_Actor getAdmin_website_actor() {
        return admin_website_actor;
    }

    public void setAdmin_website_actor(Admin_Website_Actor admin_website_actor) {
        this.admin_website_actor = admin_website_actor;
    }

}