





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Writer extends Person {

    private String name;





    private extlibrary_BookOnTape extlibrary_bookontape;


    public extlibrary_Writer(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extlibrary_BookOnTape getExtlibrary_bookontape() {
        return extlibrary_bookontape;
    }

    public void setExtlibrary_bookontape(extlibrary_BookOnTape extlibrary_bookontape) {
        this.extlibrary_bookontape = extlibrary_bookontape;
    }

}