





import java.util.List;
import java.util.ArrayList;

public class r1_ValueSetRef extends Expression {

    private String libraryName;
    private String name;



    public r1_ValueSetRef(
        String libraryName,        String name    ) {
        super(
        );
        this.libraryName = libraryName;
        this.name = name;
    }


    public String getLibraryname() {
        return libraryName;
    }

    public void setLibraryname(String libraryName) {
        this.libraryName = libraryName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}