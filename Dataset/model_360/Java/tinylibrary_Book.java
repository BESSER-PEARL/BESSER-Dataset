




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tinylibrary_Book  {

    private String damaged;
    private LocalDate published;
    private String category;
    private String isbn;
    private String pages;
    private String title;





    private tinylibrary_Library tinylibrary_library;


    public tinylibrary_Book(
        String damaged,        LocalDate published,        String category,        String isbn,        String pages,        String title    ) {
        this.damaged = damaged;
        this.published = published;
        this.category = category;
        this.isbn = isbn;
        this.pages = pages;
        this.title = title;
    }


    public String getDamaged() {
        return damaged;
    }

    public void setDamaged(String damaged) {
        this.damaged = damaged;
    }
    public LocalDate getPublished() {
        return published;
    }

    public void setPublished(LocalDate published) {
        this.published = published;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public tinylibrary_Library getTinylibrary_library() {
        return tinylibrary_library;
    }

    public void setTinylibrary_library(tinylibrary_Library tinylibrary_library) {
        this.tinylibrary_library = tinylibrary_library;
    }

}