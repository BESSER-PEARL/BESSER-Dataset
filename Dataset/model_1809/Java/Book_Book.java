





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private int nPages;
    private String title;
    private boolean isNew;
    private boolean isMultiVolume;



    public Book_Book(
        int nPages,        String title,        boolean isNew,        boolean isMultiVolume    ) {
        this.nPages = nPages;
        this.title = title;
        this.isNew = isNew;
        this.isMultiVolume = isMultiVolume;
    }


    public int getNpages() {
        return nPages;
    }

    public void setNpages(int nPages) {
        this.nPages = nPages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getIsnew() {
        return isNew;
    }

    public void setIsnew(boolean isNew) {
        this.isNew = isNew;
    }
    public boolean getIsmultivolume() {
        return isMultiVolume;
    }

    public void setIsmultivolume(boolean isMultiVolume) {
        this.isMultiVolume = isMultiVolume;
    }


}