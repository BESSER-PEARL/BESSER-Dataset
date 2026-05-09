




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_Item  {

    private LocalDate pubDate;
    private String title;





    private library_LibraryShelf library_libraryshelf;


    public library_Item(
        LocalDate pubDate,        String title    ) {
        this.pubDate = pubDate;
        this.title = title;
    }


    public LocalDate getPubdate() {
        return pubDate;
    }

    public void setPubdate(LocalDate pubDate) {
        this.pubDate = pubDate;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public library_LibraryShelf getLibrary_libraryshelf() {
        return library_libraryshelf;
    }

    public void setLibrary_libraryshelf(library_LibraryShelf library_libraryshelf) {
        this.library_libraryshelf = library_libraryshelf;
    }

}