





import java.util.List;
import java.util.ArrayList;

public class SWRC_InCollection extends Publication {

    private String edition;
    private String volume;
    private String month;
    private String address;
    private String chapter;
    private String pages;
    private String type;
    private String booktitle;
    private String number;
    private String series;



    public SWRC_InCollection(
        String edition,        String volume,        String month,        String address,        String chapter,        String pages,        String type,        String booktitle,        String number,        String series    ) {
        super(
        );
        this.edition = edition;
        this.volume = volume;
        this.month = month;
        this.address = address;
        this.chapter = chapter;
        this.pages = pages;
        this.type = type;
        this.booktitle = booktitle;
        this.number = number;
        this.series = series;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }


}