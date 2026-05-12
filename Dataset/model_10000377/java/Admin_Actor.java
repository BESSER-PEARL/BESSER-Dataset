





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Logout_UseCase logout_usecase;




    private Manage_Student___Faculty_List_UseCase manage_student___faculty_list_usecase;




    private View___Modify_the_Uploaded_Materials_UseCase view___modify_the_uploaded_materials_usecase;


    public Admin_Actor(
    ) {
    }



    public Logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(Logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }
    public Manage_Student___Faculty_List_UseCase getManage_student___faculty_list_usecase() {
        return manage_student___faculty_list_usecase;
    }

    public void setManage_student___faculty_list_usecase(Manage_Student___Faculty_List_UseCase manage_student___faculty_list_usecase) {
        this.manage_student___faculty_list_usecase = manage_student___faculty_list_usecase;
    }
    public View___Modify_the_Uploaded_Materials_UseCase getView___modify_the_uploaded_materials_usecase() {
        return view___modify_the_uploaded_materials_usecase;
    }

    public void setView___modify_the_uploaded_materials_usecase(View___Modify_the_Uploaded_Materials_UseCase view___modify_the_uploaded_materials_usecase) {
        this.view___modify_the_uploaded_materials_usecase = view___modify_the_uploaded_materials_usecase;
    }

}