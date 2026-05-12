





import java.util.List;
import java.util.ArrayList;

public class Member_Actor  {






    private Request_book_external request_book_external;




    private Inquiry_for_membership_external inquiry_for_membership_external;




    private Request_book_return_external request_book_return_external;


    public Member_Actor(
    ) {
    }



    public Request_book_external getRequest_book_external() {
        return request_book_external;
    }

    public void setRequest_book_external(Request_book_external request_book_external) {
        this.request_book_external = request_book_external;
    }
    public Inquiry_for_membership_external getInquiry_for_membership_external() {
        return inquiry_for_membership_external;
    }

    public void setInquiry_for_membership_external(Inquiry_for_membership_external inquiry_for_membership_external) {
        this.inquiry_for_membership_external = inquiry_for_membership_external;
    }
    public Request_book_return_external getRequest_book_return_external() {
        return request_book_return_external;
    }

    public void setRequest_book_return_external(Request_book_return_external request_book_return_external) {
        this.request_book_return_external = request_book_return_external;
    }

}