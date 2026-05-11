




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class web_NewsEntry extends Container {

    private String description;
    private LocalDate date;
    private String title;





    private web_Author web_author;




    private web_Site web_site;


    public web_NewsEntry(
        String description,        LocalDate date,        String title    ) {
        super(
        );
        this.description = description;
        this.date = date;
        this.title = title;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public web_Author getWeb_author() {
        return web_author;
    }

    public void setWeb_author(web_Author web_author) {
        this.web_author = web_author;
    }
    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }

}