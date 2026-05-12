





import java.util.List;
import java.util.ArrayList;

public class Patron_Actor  {






    private Check_In_Item_external check_in_item_external;




    private Check_Out_Item_external check_out_item_external;




    private Request_Book_external request_book_external;


    public Patron_Actor(
    ) {
    }



    public Check_In_Item_external getCheck_in_item_external() {
        return check_in_item_external;
    }

    public void setCheck_in_item_external(Check_In_Item_external check_in_item_external) {
        this.check_in_item_external = check_in_item_external;
    }
    public Check_Out_Item_external getCheck_out_item_external() {
        return check_out_item_external;
    }

    public void setCheck_out_item_external(Check_Out_Item_external check_out_item_external) {
        this.check_out_item_external = check_out_item_external;
    }
    public Request_Book_external getRequest_book_external() {
        return request_book_external;
    }

    public void setRequest_book_external(Request_Book_external request_book_external) {
        this.request_book_external = request_book_external;
    }

}