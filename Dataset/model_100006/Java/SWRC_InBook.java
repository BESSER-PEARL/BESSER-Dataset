





import java.util.List;
import java.util.ArrayList;

public class SWRC_InBook extends Publication {

    private String pages;
    private String address;
    private String series;
    private String number;
    private String month;
    private String chapter;
    private String type;
    private String volume;



    public SWRC_InBook(
        String pages,        String address,        String series,        String number,        String month,        String chapter,        String type,        String volume    ) {
        super(
        );
        this.pages = pages;
        this.address = address;
        this.series = series;
        this.number = number;
        this.month = month;
        this.chapter = chapter;
        this.type = type;
        this.volume = volume;
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
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }


}