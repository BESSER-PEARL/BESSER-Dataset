





import java.util.List;
import java.util.ArrayList;

public class Patron  {

    private String status;
    private int id;
    private int num_books_checked_out;
    private String address;
    private String name;



    public Patron(
        String status,        int id,        int num_books_checked_out,        String address,        String name    ) {
        this.status = status;
        this.id = id;
        this.num_books_checked_out = num_books_checked_out;
        this.address = address;
        this.name = name;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getNum_books_checked_out() {
        return num_books_checked_out;
    }

    public void setNum_books_checked_out(int num_books_checked_out) {
        this.num_books_checked_out = num_books_checked_out;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}