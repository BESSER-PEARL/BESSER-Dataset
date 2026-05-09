





import java.util.List;
import java.util.ArrayList;

public class Library3_BookInfoType  {

    private String any;





    private Library3_BookType library3_booktype;


    public Library3_BookInfoType(
        String any    ) {
        this.any = any;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public Library3_BookType getLibrary3_booktype() {
        return library3_booktype;
    }

    public void setLibrary3_booktype(Library3_BookType library3_booktype) {
        this.library3_booktype = library3_booktype;
    }

}