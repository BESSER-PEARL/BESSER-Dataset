




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_LogMessage  {

    private LocalDate clientDate;
    private LocalDate date;
    private String author;
    private String message;



    public esmodel_versioning_LogMessage(
        LocalDate clientDate,        LocalDate date,        String author,        String message    ) {
        this.clientDate = clientDate;
        this.date = date;
        this.author = author;
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


}