





import java.util.List;
import java.util.ArrayList;

public class Library  {

    private int count;
    private boolean changeSinceLastSave;
    private String file;
    private String collection;





    private LibraryGui librarygui;


    public Library(
        int count,        boolean changeSinceLastSave,        String file,        String collection    ) {
        this.count = count;
        this.changeSinceLastSave = changeSinceLastSave;
        this.file = file;
        this.collection = collection;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public boolean getChangesincelastsave() {
        return changeSinceLastSave;
    }

    public void setChangesincelastsave(boolean changeSinceLastSave) {
        this.changeSinceLastSave = changeSinceLastSave;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }

    public LibraryGui getLibrarygui() {
        return librarygui;
    }

    public void setLibrarygui(LibraryGui librarygui) {
        this.librarygui = librarygui;
    }

}