





import java.util.List;
import java.util.ArrayList;

public class Member  {

    private int id;
    private String password;
    private String name;
    private String username;





    private Book book;




    private log log;


    public Member(
        int id,        String password,        String name,        String username    ) {
        this.id = id;
        this.password = password;
        this.name = name;
        this.username = username;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
    public log getLog() {
        return log;
    }

    public void setLog(log log) {
        this.log = log;
    }

}