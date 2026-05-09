




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class addressbook_Note  {

    private String Type;
    private LocalDate Time;
    private String Comment;
    private String Author;





    private addressbook_Contact addressbook_contact;


    public addressbook_Note(
        String Type,        LocalDate Time,        String Comment,        String Author    ) {
        this.Type = Type;
        this.Time = Time;
        this.Comment = Comment;
        this.Author = Author;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public LocalDate getTime() {
        return Time;
    }

    public void setTime(LocalDate Time) {
        this.Time = Time;
    }
    public String getComment() {
        return Comment;
    }

    public void setComment(String Comment) {
        this.Comment = Comment;
    }
    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String Author) {
        this.Author = Author;
    }

    public addressbook_Contact getAddressbook_contact() {
        return addressbook_contact;
    }

    public void setAddressbook_contact(addressbook_Contact addressbook_contact) {
        this.addressbook_contact = addressbook_contact;
    }

}