





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Void_Order_UseCase void_order_usecase;




    private Login_UseCase login_usecase;




    private Make_Payment_UseCase make_payment_usecase;




    private Check_Out_UseCase check_out_usecase;




    private Add_Items_to_Cart_UseCase add_items_to_cart_usecase;




    private View_Menu_UseCase view_menu_usecase;




    private Create_Account_UseCase create_account_usecase;




    private Confirmation_e_mail_UseCase confirmation_e_mail_usecase;


    public Admin_Actor(
    ) {
    }



    public Void_Order_UseCase getVoid_order_usecase() {
        return void_order_usecase;
    }

    public void setVoid_order_usecase(Void_Order_UseCase void_order_usecase) {
        this.void_order_usecase = void_order_usecase;
    }
    public Login_UseCase getLogin_usecase() {
        return login_usecase;
    }

    public void setLogin_usecase(Login_UseCase login_usecase) {
        this.login_usecase = login_usecase;
    }
    public Make_Payment_UseCase getMake_payment_usecase() {
        return make_payment_usecase;
    }

    public void setMake_payment_usecase(Make_Payment_UseCase make_payment_usecase) {
        this.make_payment_usecase = make_payment_usecase;
    }
    public Check_Out_UseCase getCheck_out_usecase() {
        return check_out_usecase;
    }

    public void setCheck_out_usecase(Check_Out_UseCase check_out_usecase) {
        this.check_out_usecase = check_out_usecase;
    }
    public Add_Items_to_Cart_UseCase getAdd_items_to_cart_usecase() {
        return add_items_to_cart_usecase;
    }

    public void setAdd_items_to_cart_usecase(Add_Items_to_Cart_UseCase add_items_to_cart_usecase) {
        this.add_items_to_cart_usecase = add_items_to_cart_usecase;
    }
    public View_Menu_UseCase getView_menu_usecase() {
        return view_menu_usecase;
    }

    public void setView_menu_usecase(View_Menu_UseCase view_menu_usecase) {
        this.view_menu_usecase = view_menu_usecase;
    }
    public Create_Account_UseCase getCreate_account_usecase() {
        return create_account_usecase;
    }

    public void setCreate_account_usecase(Create_Account_UseCase create_account_usecase) {
        this.create_account_usecase = create_account_usecase;
    }
    public Confirmation_e_mail_UseCase getConfirmation_e_mail_usecase() {
        return confirmation_e_mail_usecase;
    }

    public void setConfirmation_e_mail_usecase(Confirmation_e_mail_UseCase confirmation_e_mail_usecase) {
        this.confirmation_e_mail_usecase = confirmation_e_mail_usecase;
    }

}