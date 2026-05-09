




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_Bookmark  {

    private String text;
    private LocalDate timestamp;
    private int page;
    private String href;
    private String id;
    private String location;





    private library_Book library_book;


    public library_Bookmark(
        String text,        LocalDate timestamp,        int page,        String href,        String id,        String location    ) {
        this.text = text;
        this.timestamp = timestamp;
        this.page = page;
        this.href = href;
        this.id = id;
        this.location = location;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }
    public int getPage() {
        return page;
    }

    public void setPage(int page) {
        this.page = page;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }

}