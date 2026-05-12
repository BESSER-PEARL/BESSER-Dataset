





import java.util.List;
import java.util.ArrayList;

public class LibraryGui  {

    private None libraryController;
    private None library;





    private LibraryController librarycontroller;


    public LibraryGui(
        None libraryController,        None library    ) {
        this.libraryController = libraryController;
        this.library = library;
    }


    public None getLibrarycontroller() {
        return libraryController;
    }

    public void setLibrarycontroller(None libraryController) {
        this.libraryController = libraryController;
    }
    public None getLibrary() {
        return library;
    }

    public void setLibrary(None library) {
        this.library = library;
    }

    public LibraryController getLibrarycontroller() {
        return librarycontroller;
    }

    public void setLibrarycontroller(LibraryController librarycontroller) {
        this.librarycontroller = librarycontroller;
    }

}