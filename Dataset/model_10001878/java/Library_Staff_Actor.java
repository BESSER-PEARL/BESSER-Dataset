





import java.util.List;
import java.util.ArrayList;

public class Library_Staff_Actor  {






    private Organize_Books_external organize_books_external;




    private Manage_Computer_Terminals_external manage_computer_terminals_external;




    private Reserve_Book_For_Semester_external reserve_book_for_semester_external;




    private Manage_Reference_Materials_external manage_reference_materials_external;




    private Renew_Magazine_Subscriptions_external renew_magazine_subscriptions_external;




    private Order_New_Resources_external order_new_resources_external;


    public Library_Staff_Actor(
    ) {
    }



    public Organize_Books_external getOrganize_books_external() {
        return organize_books_external;
    }

    public void setOrganize_books_external(Organize_Books_external organize_books_external) {
        this.organize_books_external = organize_books_external;
    }
    public Manage_Computer_Terminals_external getManage_computer_terminals_external() {
        return manage_computer_terminals_external;
    }

    public void setManage_computer_terminals_external(Manage_Computer_Terminals_external manage_computer_terminals_external) {
        this.manage_computer_terminals_external = manage_computer_terminals_external;
    }
    public Reserve_Book_For_Semester_external getReserve_book_for_semester_external() {
        return reserve_book_for_semester_external;
    }

    public void setReserve_book_for_semester_external(Reserve_Book_For_Semester_external reserve_book_for_semester_external) {
        this.reserve_book_for_semester_external = reserve_book_for_semester_external;
    }
    public Manage_Reference_Materials_external getManage_reference_materials_external() {
        return manage_reference_materials_external;
    }

    public void setManage_reference_materials_external(Manage_Reference_Materials_external manage_reference_materials_external) {
        this.manage_reference_materials_external = manage_reference_materials_external;
    }
    public Renew_Magazine_Subscriptions_external getRenew_magazine_subscriptions_external() {
        return renew_magazine_subscriptions_external;
    }

    public void setRenew_magazine_subscriptions_external(Renew_Magazine_Subscriptions_external renew_magazine_subscriptions_external) {
        this.renew_magazine_subscriptions_external = renew_magazine_subscriptions_external;
    }
    public Order_New_Resources_external getOrder_new_resources_external() {
        return order_new_resources_external;
    }

    public void setOrder_new_resources_external(Order_New_Resources_external order_new_resources_external) {
        this.order_new_resources_external = order_new_resources_external;
    }

}