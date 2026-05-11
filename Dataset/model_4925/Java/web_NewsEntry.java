




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class web_NewsEntry extends Container {

    private String title;
    private String description;
    private LocalDate date;





    private web_Site web_site;


    public web_NewsEntry(
        String title,        String description,        LocalDate date    ) {
        super(
        );
        this.title = title;
        this.description = description;
        this.date = date;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
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

    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }

}