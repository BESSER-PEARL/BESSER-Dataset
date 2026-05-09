




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_LogMessage  {

    private LocalDate clientDate;
    private String author;
    private LocalDate date;
    private String message;



    public esmodel_versioning_LogMessage(
        LocalDate clientDate,        String author,        LocalDate date,        String message    ) {
        this.clientDate = clientDate;
        this.author = author;
        this.date = date;
        this.message = message;
    }


    public LocalDate getClientdate() {
        return clientDate;
    }

    public void setClientdate(LocalDate clientDate) {
        this.clientDate = clientDate;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
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


}