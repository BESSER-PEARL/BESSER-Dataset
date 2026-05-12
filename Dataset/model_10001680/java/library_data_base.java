





import java.util.List;
import java.util.ArrayList;

public class library_data_base  {

    private int record_patron_borrowing_book;
    private String members_information;
    private String list_of_books;



    public library_data_base(
        int record_patron_borrowing_book,        String members_information,        String list_of_books    ) {
        this.record_patron_borrowing_book = record_patron_borrowing_book;
        this.members_information = members_information;
        this.list_of_books = list_of_books;
    }


    public int getRecord_patron_borrowing_book() {
        return record_patron_borrowing_book;
    }

    public void setRecord_patron_borrowing_book(int record_patron_borrowing_book) {
        this.record_patron_borrowing_book = record_patron_borrowing_book;
    }
    public String getMembers_information() {
        return members_information;
    }

    public void setMembers_information(String members_information) {
        this.members_information = members_information;
    }
    public String getList_of_books() {
        return list_of_books;
    }

    public void setList_of_books(String list_of_books) {
        this.list_of_books = list_of_books;
    }


}