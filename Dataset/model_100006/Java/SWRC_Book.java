





import java.util.List;
import java.util.ArrayList;

public class SWRC_Book extends Publication {

    private String number;
    private String price;
    private String volume;
    private String month;
    private String edition;
    private String source;
    private String series;
    private String isbn;
    private String address;



    public SWRC_Book(
        String number,        String price,        String volume,        String month,        String edition,        String source,        String series,        String isbn,        String address    ) {
        super(
        );
        this.number = number;
        this.price = price;
        this.volume = volume;
        this.month = month;
        this.edition = edition;
        this.source = source;
        this.series = series;
        this.isbn = isbn;
        this.address = address;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}