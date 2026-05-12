





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private insert_record_UseCase insert_record_usecase;




    private Logout_UseCase logout_usecase;




    private generate_report_UseCase generate_report_usecase;




    private update_record_UseCase update_record_usecase;




    private Login_UseCase login_usecase;


    public Admin_Actor(
    ) {
    }



    public insert_record_UseCase getInsert_record_usecase() {
        return insert_record_usecase;
    }

    public void setInsert_record_usecase(insert_record_UseCase insert_record_usecase) {
        this.insert_record_usecase = insert_record_usecase;
    }
    public Logout_UseCase getLogout_usecase() {
        return logout_usecase;
    }

    public void setLogout_usecase(Logout_UseCase logout_usecase) {
        this.logout_usecase = logout_usecase;
    }
    public generate_report_UseCase getGenerate_report_usecase() {
        return generate_report_usecase;
    }

    public void setGenerate_report_usecase(generate_report_UseCase generate_report_usecase) {
        this.generate_report_usecase = generate_report_usecase;
    }
    public update_record_UseCase getUpdate_record_usecase() {
        return update_record_usecase;
    }

    public void setUpdate_record_usecase(update_record_UseCase update_record_usecase) {
        this.update_record_usecase = update_record_usecase;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }

}