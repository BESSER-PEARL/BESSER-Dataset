





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int adminID;
    private String name;
    private String email;
    private String password;
    private String phoneNo;





    private List<BooksOrder> booksorders;


    public Administrator(
        int adminID,        String name,        String email,        String password,        String phoneNo    ) {
        this.adminID = adminID;
        this.name = name;
        this.email = email;
        this.password = password;
        this.phoneNo = phoneNo;
        this.booksorders = new ArrayList<>();
    }

    public Administrator(
        int adminID,        String name,        String email,        String password,        String phoneNo        ArrayList<BooksOrder> booksorders    ) {
        this.adminID = adminID;
        this.name = name;
        this.email = email;
        this.password = password;
        this.phoneNo = phoneNo;
        this.booksorders = booksorders;
    }

    public int getAdminid() {
        return adminID;
    }

    public void setAdminid(int adminID) {
        this.adminID = adminID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public List<BooksOrder> getBooksorders() {
        return booksorders;
    }

    public void addBooksorder(Booksorder booksorder) {
        this.booksorders.add(booksorder);
    }

}