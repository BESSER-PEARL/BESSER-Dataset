





import java.util.List;
import java.util.ArrayList;

public class publisher  {

    private int id;
    private String address;
    private String email;
    private String name;
    private String website;





    private book book;




    private DBA dba;


    public publisher(
        int id,        String address,        String email,        String name,        String website    ) {
        this.id = id;
        this.address = address;
        this.email = email;
        this.name = name;
        this.website = website;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }
    public DBA getDba() {
        return dba;
    }

    public void setDba(DBA dba) {
        this.dba = dba;
    }

}