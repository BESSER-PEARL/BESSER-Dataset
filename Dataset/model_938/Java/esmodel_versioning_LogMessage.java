




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_LogMessage  {

    private LocalDate date;
    private String message;
    private String author;
    private LocalDate clientDate;



    public esmodel_versioning_LogMessage(
        LocalDate date,        String message,        String author,        LocalDate clientDate    ) {
        this.date = date;
        this.message = message;
        this.author = author;
        this.clientDate = clientDate;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }


}