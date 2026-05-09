





import java.util.List;
import java.util.ArrayList;

public class sunBooks_BookType  {

    private String bookCategory;
    private String description;
    private String itemId;
    private String publicationDate;
    private String name;
    private String iSBN;
    private String price;





    private sunBooks_AuthorsType sunbooks_authorstype;




    private sunBooks_BooksType sunbooks_bookstype;


    public sunBooks_BookType(
        String bookCategory,        String description,        String itemId,        String publicationDate,        String name,        String iSBN,        String price    ) {
        this.bookCategory = bookCategory;
        this.description = description;
        this.itemId = itemId;
        this.publicationDate = publicationDate;
        this.name = name;
        this.iSBN = iSBN;
        this.price = price;
    }


    public String getBookcategory() {
        return bookCategory;
    }

    public void setBookcategory(String bookCategory) {
        this.bookCategory = bookCategory;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getItemid() {
        return itemId;
    }

    public void setItemid(String itemId) {
        this.itemId = itemId;
    }
    public String getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(String publicationDate) {
        this.publicationDate = publicationDate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsbn() {
        return iSBN;
    }

    public void setIsbn(String iSBN) {
        this.iSBN = iSBN;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public sunBooks_AuthorsType getSunbooks_authorstype() {
        return sunbooks_authorstype;
    }

    public void setSunbooks_authorstype(sunBooks_AuthorsType sunbooks_authorstype) {
        this.sunbooks_authorstype = sunbooks_authorstype;
    }
    public sunBooks_BooksType getSunbooks_bookstype() {
        return sunbooks_bookstype;
    }

    public void setSunbooks_bookstype(sunBooks_BooksType sunbooks_bookstype) {
        this.sunbooks_bookstype = sunbooks_bookstype;
    }

}