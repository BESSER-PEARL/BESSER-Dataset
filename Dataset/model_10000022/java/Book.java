





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String realese_date;
    private int pages;
    private String autor;
    private String name;



    public Book(
        String realese_date,        int pages,        String autor,        String name    ) {
        this.realese_date = realese_date;
        this.pages = pages;
        this.autor = autor;
        this.name = name;
    }


    public String getRealese_date() {
        return realese_date;
    }

    public void setRealese_date(String realese_date) {
        this.realese_date = realese_date;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}