





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private int Price;
    private String BookName;
    private String PubName;
    private int BookID;
    private int LibraryID;



    public Book(
        int Price,        String BookName,        String PubName,        int BookID,        int LibraryID    ) {
        this.Price = Price;
        this.BookName = BookName;
        this.PubName = PubName;
        this.BookID = BookID;
        this.LibraryID = LibraryID;
    }


    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }
    public String getBookname() {
        return BookName;
    }

    public void setBookname(String BookName) {
        this.BookName = BookName;
    }
    public String getPubname() {
        return PubName;
    }

    public void setPubname(String PubName) {
        this.PubName = PubName;
    }
    public int getBookid() {
        return BookID;
    }

    public void setBookid(int BookID) {
        this.BookID = BookID;
    }
    public int getLibraryid() {
        return LibraryID;
    }

    public void setLibraryid(int LibraryID) {
        this.LibraryID = LibraryID;
    }


}