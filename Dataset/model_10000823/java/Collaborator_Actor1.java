





import java.util.List;
import java.util.ArrayList;

public class Collaborator_Actor1  {






    private Update_an_Expense_external update_an_expense_external;




    private Create_an_Expense_external create_an_expense_external;




    private Manage_attached_files_UseCase manage_attached_files_usecase;


    public Collaborator_Actor1(
    ) {
    }



    public Update_an_Expense_external getUpdate_an_expense_external() {
        return update_an_expense_external;
    }

    public void setUpdate_an_expense_external(Update_an_Expense_external update_an_expense_external) {
        this.update_an_expense_external = update_an_expense_external;
    }
    public Create_an_Expense_external getCreate_an_expense_external() {
        return create_an_expense_external;
    }

    public void setCreate_an_expense_external(Create_an_Expense_external create_an_expense_external) {
        this.create_an_expense_external = create_an_expense_external;
    }
    public Manage_attached_files_UseCase getManage_attached_files_usecase() {
        return manage_attached_files_usecase;
    }

    public void setManage_attached_files_usecase(Manage_attached_files_UseCase manage_attached_files_usecase) {
        this.manage_attached_files_usecase = manage_attached_files_usecase;
    }

}