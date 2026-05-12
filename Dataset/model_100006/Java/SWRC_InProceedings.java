





import java.util.List;
import java.util.ArrayList;

public class SWRC_InProceedings extends Publication {

    private String volume;
    private String series;
    private String pages;
    private String address;
    private String month;
    private String number;
    private String booktitle;



    public SWRC_InProceedings(
        String volume,        String series,        String pages,        String address,        String month,        String number,        String booktitle    ) {
        super(
        );
        this.volume = volume;
        this.series = series;
        this.pages = pages;
        this.address = address;
        this.month = month;
        this.number = number;
        this.booktitle = booktitle;
    }


    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }


}