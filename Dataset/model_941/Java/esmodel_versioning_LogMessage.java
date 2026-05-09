




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_LogMessage  {

    private String author;
    private String message;
    private LocalDate clientDate;
    private LocalDate date;



    public esmodel_versioning_LogMessage(
        String author,        String message,        LocalDate clientDate,        LocalDate date    ) {
        this.author = author;
        this.message = message;
        this.clientDate = clientDate;
        this.date = date;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}