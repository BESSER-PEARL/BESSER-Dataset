





import java.util.List;
import java.util.ArrayList;

public class r1_CodeSystemRef extends Expression {

    private String name;
    private String libraryName;



    public r1_CodeSystemRef(
        String name,        String libraryName    ) {
        super(
        );
        this.name = name;
        this.libraryName = libraryName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLibraryname() {
        return libraryName;
    }

    public void setLibraryname(String libraryName) {
        this.libraryName = libraryName;
    }


}