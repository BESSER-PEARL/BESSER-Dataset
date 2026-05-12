





import java.util.List;
import java.util.ArrayList;

public class bibTeX_AddressField  {

    private String address;





    private bibTeX_Book bibtex_book;


    public bibTeX_AddressField(
        String address    ) {
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public bibTeX_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibTeX_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}