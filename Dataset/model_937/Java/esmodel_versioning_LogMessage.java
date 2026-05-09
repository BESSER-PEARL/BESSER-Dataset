




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_LogMessage  {

    private LocalDate date;
    private String message;
    private LocalDate clientDate;
    private String author;



    public esmodel_versioning_LogMessage(
        LocalDate date,        String message,        LocalDate clientDate,        String author    ) {
        this.date = date;
        this.message = message;
        this.clientDate = clientDate;
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


}