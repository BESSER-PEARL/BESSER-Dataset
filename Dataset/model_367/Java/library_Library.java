





import java.util.List;
import java.util.ArrayList;

public class library_Library extends Addressable {

    private String name;



    public library_Library(
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


}