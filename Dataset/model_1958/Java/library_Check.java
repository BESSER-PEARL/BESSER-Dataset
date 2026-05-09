





import java.util.List;
import java.util.ArrayList;

public class library_Check extends Command {

    private String isbn;



    public library_Check(
        String isbn    ) {
        super(
        );
        this.isbn = isbn;
    }


    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


}